import logging
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core import security
from app.core.security import decode_access_token
from app.models.users import User
from app.schemas.auth import UserRegister, UserLogin, TokenResponse
from app.schemas.users import UserRead

router = APIRouter(prefix="/auth", tags=["Authentication"])
logger = logging.getLogger(__name__)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
) -> User:
    """Decode JWT from Bearer token, fetch user, and return User object."""
    user_id = decode_access_token(token)
    user = db.query(User).filter(user_id == User.id).first()
    if not user:
        logger.warning("User not found with id=%s", user_id)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User no longer exists"
        )
    return user


@router.post("/register", response_model=UserRead,
             summary="Register a new user",
             response_description="The newly created user with ID")
def register_user(
        user_data: UserRegister,
        db: Session = Depends(get_db)
):
    """
    Registers a new user with a username, password, and role.
    Roles can be 'admin', 'jury', or 'participant'.
    """
    existing = db.query(User).filter(user_data.username == User.username).first()
    if existing:
        logger.info("Attempt to register duplicate username: %s", user_data.username)
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed = security.hash_password(user_data.password)
    new_user = User(
        username=user_data.username,
        password_hash=hashed,
        role=user_data.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    logger.info("New user registered: %s", new_user.username)
    return new_user


@router.post("/login", response_model=TokenResponse,
             summary="Login to obtain JWT token",
             response_description="JWT token for subsequent requests")
def login_user(
        login_data: UserLogin,
        db: Session = Depends(get_db)
):
    """Logs in a user with username/password. Returns an access token if valid."""
    db_user = db.query(User).filter(login_data.username == User.username).first()
    if not db_user or not security.verify_password(login_data.password, db_user.password_hash):
        logger.warning("Invalid login attempt for user=%s", login_data.username)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    access_token = security.create_access_token(subject=str(db_user.id))
    logger.info("User logged in: %s (role=%s)", db_user.username, db_user.role)
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": db_user.role
    }
