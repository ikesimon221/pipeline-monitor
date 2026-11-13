from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.segment import Segment
from app.schemas.segment import SegmentOut

router = APIRouter(prefix="/segments", tags=["segments"])

@router.get("/", response_model=List[SegmentOut])
def list_segments(db: Session = Depends(get_db)):
    return db.query(Segment).order_by(Segment.id).all()
