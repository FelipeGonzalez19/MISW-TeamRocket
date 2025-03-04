from sqlalchemy.orm import Session
from .models import Usuario
from fastapi import HTTPException

class UsuarioRepositorio:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def guardar(self, usuario: Usuario):
        self.db_session.add(usuario)
        self.db_session.commit()

    def obtener_por_id(self, usuario_id: str):
        return self.db_session.query(Usuario).filter(Usuario.id == usuario_id).first()

    def obtener_por_email(self, email: str):
        return self.db_session.query(Usuario).filter(Usuario.email == email).first()

    def obtener_todos(self):
        return self.db_session.query(Usuario).all()
