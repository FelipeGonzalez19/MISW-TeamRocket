from .database import Base
from sqlalchemy import Column, String, Integer, Float, DateTime
from datetime import datetime

class MonetizacionRegistro(Base):
    __tablename__ = "monetizacion_registro"

    id = Column(String, primary_key=True, index=True)
    imagen_id = Column(String, nullable=False, index=True)
    usuario_id = Column(String, nullable=False)
    accesos = Column(Integer, default=0)
    valor_por_acceso = Column(Float, nullable=False)
    total_pagar = Column(Float, default=0)
    fecha_actualizacion = Column(DateTime, default=datetime.utcnow)
