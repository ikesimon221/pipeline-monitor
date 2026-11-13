from pydantic import BaseModel, ConfigDict

class SegmentOut(BaseModel):
    id: int
    name: str
    pressure_min: float
    pressure_max: float
    temperature_min: float
    temperature_max: float
    flow_min: float
    flow_max: float

    # Lets Pydantic build this from a database row, not just from a dictionary
    model_config = ConfigDict(from_attributes=True)