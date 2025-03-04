from .database import Base
from sqlalchemy import Column, String, Integer

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(String, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    intentos_login = Column(Integer, default=0)
