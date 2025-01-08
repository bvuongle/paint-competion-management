from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, func
from app.core.database import Base


class Threshold(Base):
    __tablename__ = "thresholds"

    id = Column(Integer, primary_key=True, index=True)
    stage_id = Column(Integer, ForeignKey("stage.id", ondelete="CASCADE"), nullable=False)
    min_score = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
