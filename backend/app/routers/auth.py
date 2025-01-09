import logging
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import hash_password, verify_password, create_access_token, VALID_ROLES
from app.core.config import settings
from app.models.users import User
from app.schemas.auth import UserRegister, UserLogin, TokenResponse
from app.schemas.users import UserRead

router = APIRouter(prefix="/auth", tags=["Authentication"])
logger = logging.getLogger(__name__)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


@router.post("/register", response_model=UserRead,
             summary="Register a new user",
             response_description="The newly created user with ID")
def register_user(
        user_data: UserRegister,
        db: Session = Depends(get_db)
):
    """
    Registers a new user with a username, password, and role.
    Roles must be one of 'admin', 'jury', or 'participant'.
    """
    if user_data.role not in VALID_ROLES:
        raise HTTPException(status_code=400, detail=f"Invalid role: {user_data.role}")

    existing = db.query(User).filter(user_data.username == User.username).first()
    if existing:
        logger.info("Attempt to register duplicate username: %s", user_data.username)
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed = hash_password(user_data.password, pepper=settings.PEPPER)
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
    if not db_user:
        logger.warning("Username does not exist: %s", login_data.username)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    if not verify_password(login_data.password, db_user.password_hash.value, pepper=settings.PEPPER):
        logger.warning("Incorrect password for user=%s", login_data.username)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    access_token = create_access_token(subject=str(db_user.id))
    logger.info("User logged in: %s (role=%s)", db_user.username, db_user.role)
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": db_user.role
    }
