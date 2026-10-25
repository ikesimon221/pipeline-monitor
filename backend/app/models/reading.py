from sqlalchemy import Column, Integer, Float, Boolean, DateTime, ForeignKey, Index
from sqlalchemy.sql import func
from app.database import Base

class Reading(Base):
    __tablename__ = "readings"

    id = Column(Integer, primary_key=True, index=True)

    # Which pipeline segment this reading came from
    segment_id = Column(Integer, ForeignKey("segments.id"), nullable=False)

    # The three sensor values
    pressure = Column(Float, nullable=False)      # in bar
    temperature = Column(Float, nullable=False)   # in degrees Celsius
    flow_rate = Column(Float, nullable=False)     # in cubic metres per hour

    # True if any value was outside the segment's safe range
    is_anomaly = Column(Boolean, default=False, nullable=False)

    # The database fills this in with the current time when a row is saved
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Speeds up the query we'll run most: the newest readings for one segment
    __table_args__ = (
        Index("ix_readings_segment_time", "segment_id", "created_at"),
    )