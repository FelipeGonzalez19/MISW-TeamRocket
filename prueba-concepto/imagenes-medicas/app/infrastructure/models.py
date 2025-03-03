#app/infrastructure/models.py

from .database import Base  
from sqlalchemy import Column, String, JSON,Index
from pydantic import BaseModel
from sqlalchemy.orm import deferred
from typing import Dict, Any

class ImagenMedicaDB(Base):
    __tablename__ = "imagenes_medicas"

    id = Column(String, primary_key=True, index=True)
    tipo_imagen = Column(String, nullable=False, index=True)
    region_anatomica = Column(String, nullable=False, index=True)
    data = deferred(Column(JSON, nullable=False))

    __table_args__ = (
        Index('idx_tipo_imagen', 'tipo_imagen'),
        Index('idx_region_anatomica', 'region_anatomica'),
        Index('idx_tipo_region', 'tipo_imagen', 'region_anatomica') 
    )
class ImagenInputDTO(BaseModel):
    id: str
    tipo_imagen: str
    region_anatomica: str
    data: Dict[str, Any]
    origen_datos:str
    
    