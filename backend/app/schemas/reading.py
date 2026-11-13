from datetime import datetime
from pydantic import BaseModel, ConfigDict

class ReadingOut(BaseModel):
    id: int
    segment_id: int
    pressure: float
    temperature: float
    flow_rate: float
    is_anomaly: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)