import logging
from typing import Type, List

from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.core.config import settings
from app.core.constant import VALID_ROLES
from app.core.database import get_db
from app.models.users import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
logger = logging.getLogger(__name__)


def hash_password(password: str, pepper: str = "") -> str:
    """ Hash a plaintext password using bcrypt. """
    return pwd_context.hash(password + pepper)


def verify_password(plain: str, hashed: str, pepper: str = "") -> bool:
    """
    Verify a plaintext password against the hashed value.
    """
    return pwd_context.verify(plain + pepper, hashed)


def create_access_token(subject: str, expires_minutes: int = 60) -> str:
    """
    Create a JWT token with a default expiration of 60 minutes.
    The 'sub' field in the payload will store the user_id as a string.
    """
    to_encode = {
        "sub": subject,
        "exp": datetime.utcnow() + timedelta(minutes=expires_minutes)
    }
    encoded_jwt = jwt.encode(
        to_encode,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )
    logger.info("Access token created for user_id=%s", subject)
    return encoded_jwt


def decode_access_token(token: str) -> str:
    """
    Decode the JWT and return the user ID (subject).
    Raises HTTP 401 if invalid or expired.
    """
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token: missing user ID"
            )
        return user_id
    except JWTError as e:
        logger.warning("JWT decode error: %s", e)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )


def get_current_user(token: str, db: Session) -> Type[User]:
    """
    Internal helper that decodes a token, fetches the user from DB,
    raises 401 if user not found or inactive, etc.
    """
    user_id = decode_access_token(token)
    user = db.query(User).filter(user_id == User.id).first()
    if not user:
        logger.warning("User not found with id=%s", user_id)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User no longer exists"
        )
    return user


def requires_roles(*allowed_roles: List[str]):
    """
    A dependency generator. Usage:

    Extract the bearer token (OAuth2PasswordBearer).
    Decode the user, ensure user.role is in allowed_roles.
    Return the user object if all checks pass.
    """
    from fastapi.security import OAuth2PasswordBearer
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

    def role_dependency(token: str = Depends(oauth2_scheme),
                        db: Session = Depends(get_db)) -> Type[User]:
        user = get_current_user(token, db)

        if allowed_roles:
            if user.role not in allowed_roles:
                logger.warning("User %s tried to access endpoint requiring %s",
                               user.username, allowed_roles)
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Requires role(s): {', '.join(allowed_roles)}"
                )

        if user.role not in VALID_ROLES:
            logger.error("User %s has invalid role: %s", user.username, user.role)
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid role in system"
            )

        return user

    return role_dependency
