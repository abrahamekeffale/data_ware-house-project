from sqlalchemy.orm import Session
from . import models, schemas

def get_detection_results(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.DetectionResult).offset(skip).limit(limit).all()

def create_detection_result(db: Session, detection: schemas.DetectionResultCreate):
    db_detection = models.DetectionResult(**detection.dict())
    db.add(db_detection)
    db.commit()
    db.refresh(db_detection)
    return db_detection
