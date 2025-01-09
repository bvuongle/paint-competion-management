import logging
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.users import User
from app.schemas.users import UserBase, UserRead
from app.core.security import requires_roles

router = APIRouter(prefix="/users", tags=["Users"])
logger = logging.getLogger(__name__)


@router.get("/", response_model=List[UserRead],
            summary="List all users",
            response_description="A list of all registered users.")
def list_users(
        db: Session = Depends(get_db),
        current_user: User = Depends(requires_roles("admin"))
    ) -> List[User]:
    """
    Returns all users in the system.
    Only an admin can list all users.
    """
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    users = db.query(User).all()
    logger.info("Admin %s listed all users", current_user.username)
    return users


@router.put("/{user_id}", response_model=UserRead,
            summary="Update a user account",
            response_description="The updated user.")
def update_user(
        user_id: int,
        user_data: UserBase,
        db: Session = Depends(get_db),
        current_user: User = Depends(requires_roles(["admin"]))
):
    """
    Allows an admin to update a user's username or role.
    Note: This doesn't change password; a separate endpoint or a password reset flow would do that.
    """
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    db_user = db.query(User).filter(user_id == User.id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Update fields
    db_user.username = user_data.username
    db_user.role = user_data.role
    db.commit()
    db.refresh(db_user)
    logger.info("Admin %s updated user %s", current_user.username, db_user.username)
    return db_user


@router.delete("/{user_id}", status_code=204, summary="Delete a user account")
def delete_user(
        user_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(requires_roles(["admin"]))
):
    """
    Allows admin to delete a user from the system.
    Returns no content on success.
    """
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    db_user = db.query(User).filter(user_id == User.id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(db_user)
    db.commit()
    logger.info("Admin %s deleted user with id=%d", current_user.username, user_id)
    return
