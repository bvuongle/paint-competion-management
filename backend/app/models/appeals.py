from sqlalchemy import Column, Integer, Text, Boolean, DateTime, ForeignKey, func
from backend.app.core.database import Base


class Appeal(Base):
    __tablename__ = "appeals"

    id = Column(Integer, primary_key=True, index=True)
    score_id = Column(Integer, ForeignKey("scores.id", ondelete="CASCADE"), nullable=False)
    appeal_text = Column(Text, nullable=False)
    jury_response = Column(Text, nullable=True)
    is_resolved = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
