from sqlalchemy import Column, Integer, String, Float
from .database import Base

class DetectionResult(Base):
    __tablename__ = 'detection_results'

    id = Column(Integer, primary_key=True, index=True)
    image_name = Column(String, index=True)
    class_label = Column(String, index=True)
    confidence_score = Column(Float)
    bbox_coordinates = Column(String)
