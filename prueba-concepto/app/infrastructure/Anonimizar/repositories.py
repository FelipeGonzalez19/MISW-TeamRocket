from sqlalchemy.orm import Session
from .models import AnonimizacionRegistro
from fastapi import HTTPException

class AnonimizacionRepositorio:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def guardar(self, registro: AnonimizacionRegistro):
        self.db_session.add(registro)
        self.db_session.commit()

    def obtener_por_id(self, anonimizacion_id: str):
        return self.db_session.query(AnonimizacionRegistro).filter(AnonimizacionRegistro.id == anonimizacion_id).first()

    def obtener_todas(self):
        return self.db_session.query(AnonimizacionRegistro).all()
