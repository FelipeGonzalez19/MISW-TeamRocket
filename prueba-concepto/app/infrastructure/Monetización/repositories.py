from sqlalchemy.orm import Session
from .models import MonetizacionRegistro
from fastapi import HTTPException

class MonetizacionRepositorio:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def guardar(self, registro: MonetizacionRegistro):
        self.db_session.add(registro)
        self.db_session.commit()

    def obtener_por_id(self, monetizacion_id: str):
        return self.db_session.query(MonetizacionRegistro).filter(MonetizacionRegistro.id == monetizacion_id).first()

    def obtener_todos(self):
        return self.db_session.query(MonetizacionRegistro).all()
