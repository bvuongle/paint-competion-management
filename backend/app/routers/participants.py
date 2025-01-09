import logging
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import requires_roles
from app.models.participants import Participant
from app.models.users import User
from app.schemas.participants import ParticipantCreate, ParticipantRead

router = APIRouter(prefix="/participants", tags=["Participants"])
logger = logging.getLogger(__name__)


@router.get("/", response_model=List[ParticipantRead],
            summary="List all participants",
            response_description="List of participants.")
def list_participants(
        db: Session = Depends(get_db),
        current_user: User = Depends(requires_roles("admin", "jury"))
):
    """
    Returns all participants in the system.
    Admin or jury can view all participants;
    participants can view as well if you want to keep it open.
    Adjust the role check as needed.
    """
    parts = db.query(Participant).all()
    logger.info("User=%s listed all participants", current_user.username)
    return parts


@router.post("/", response_model=ParticipantRead,
             summary="Create a new participant",
             response_description="The newly created participant.")
def create_participant(
        participant_data: ParticipantCreate,
        db: Session = Depends(get_db),
        current_user: User = Depends(requires_roles("admin", "jury"))
):
    """
    Creates a new participant entry. Typically only an admin or jury might do this.
    """
    new_participant = Participant(**participant_data.dict())
    db.add(new_participant)
    db.commit()
    db.refresh(new_participant)
    logger.info("User=%s created participant id=%d", current_user.username, new_participant.id)
    return new_participant

@router.get("/{participant_id}", response_model=ParticipantRead,
            summary="Get a single participant by ID",
            response_description="A single participant's data.")
def get_participant(
        participant_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(requires_roles(["admin", "jury", "participant"]))
):
    """
    Retrieves details for a single participant by ID.
    """
    participant = db.query(Participant).filter(participant_id == Participant.id).first()
    if not participant:
        logger.warning("Participant not found with id=%d", participant_id)
        raise HTTPException(status_code=404, detail="Participant not found")
    return participant


@router.put("/{participant_id}", response_model=ParticipantRead,
            summary="Update a participant",
            response_description="The updated participant data.")
def update_participant(
        participant_id: int,
        participant_data: ParticipantCreate,
        db: Session = Depends(get_db),
        current_user: User = Depends(requires_roles("admin", "jury"))
):
    """
    Updates participant data.
    """
    participant = db.query(Participant).filter(participant_id == Participant.id).first()
    if not participant:
        raise HTTPException(status_code=404, detail="Participant not found")

    for field, value in participant_data.dict().items():
        setattr(participant, field, value)
    db.commit()
    db.refresh(participant)
    logger.info("User=%s updated participant id=%d", current_user.username, participant.id)
    return participant


@router.delete("/{participant_id}", status_code=204, summary="Delete a participant")
def delete_participant(
        participant_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(requires_roles("admin", "jury"))
):
    """
    Delete a participant from the system.
    """
    participant = db.query(Participant).filter(participant_id == Participant.id).first()
    if not participant:
        raise HTTPException(status_code=404, detail="Participant not found")

    db.delete(participant)
    db.commit()
    logger.info("User=%s deleted participant id=%d", current_user.username, participant_id)
    return
