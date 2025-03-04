from .database import Base
from sqlalchemy import Column, String, DateTime
from datetime import datetime

class AnonimizacionRegistro(Base):
    __tablename__ = "anonimizacion_registro"

    id = Column(String, primary_key=True, index=True)
    imagen_id = Column(String, nullable=False, index=True)
    estado = Column(String, nullable=False, default="pendiente")  # pendiente, anonimizado, error
    fecha_procesamiento = Column(DateTime, default=datetime.utcnow)
