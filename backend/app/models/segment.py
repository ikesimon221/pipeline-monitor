from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Segment(Base):
    # The name of the table in the database
    __tablename__ = "segments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    # Safe operating limits. A reading outside these will be flagged.
    pressure_min = Column(Float, nullable=False)     # in bar
    pressure_max = Column(Float, nullable=False)
    temperature_min = Column(Float, nullable=False)  # in degrees Celsius
    temperature_max = Column(Float, nullable=False)
    flow_min = Column(Float, nullable=False)         # in cubic metres per hour
    flow_max = Column(Float, nullable=False)