from pydantic import BaseModel

class DetectionResultBase(BaseModel):
    image_name: str
    class_label: str
    confidence_score: float
    bbox_coordinates: str

class DetectionResultCreate(DetectionResultBase):
    pass

class DetectionResult(DetectionResultBase):
    id: int

    class Config:
        orm_mode = True
