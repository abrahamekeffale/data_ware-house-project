from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new detection result
@app.post("/detection/", response_model=schemas.DetectionResult)
def create_detection(detection: schemas.DetectionResultCreate, db: Session = Depends(get_db)):
    return crud.create_detection_result(db=db, detection=detection)

# Retrieve detection results
@app.get("/detection/", response_model=list[schemas.DetectionResult])
def read_detections(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    detections = crud.get_detection_results(db, skip=skip, limit=limit)
    return detections
