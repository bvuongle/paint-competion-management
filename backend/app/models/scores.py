from sqlalchemy import Column, Integer, Float, Boolean, Text, DateTime, ForeignKey, func
from backend.app.core.database import Base


class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, index=True)
    participant_id = Column(Integer, ForeignKey("participants.id", ondelete="CASCADE"), nullable=False)
    jury_id = Column(Integer, ForeignKey("jury.id", ondelete="CASCADE"), nullable=False)
    stage_id = Column(Integer, ForeignKey("stage.id", ondelete="CASCADE"), nullable=False)
    points = Column(Float, nullable=False, default=0.0)
    is_final = Column(Boolean, default=False)
    comments = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
