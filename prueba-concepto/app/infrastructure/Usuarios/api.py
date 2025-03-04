from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from ...application.services import UsuarioService
from ...application.commands import RegistrarUsuarioCommand, ObtenerUsuarioQuery
from .repositories import UsuarioRepositorio
from .database import get_db

app = FastAPI()

def get_repo(db: Session = Depends(get_db)):
    return UsuarioRepositorio(db)

def get_service(repo: UsuarioRepositorio = Depends(get_repo)):
    return UsuarioService(repo)

@app.post("/usuarios")
def registrar_usuario(usuario_data: dict, service: UsuarioService = Depends(get_service)):
    command = RegistrarUsuarioCommand(usuario_data)
    return service.registrar_usuario(command)

@app.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: str, service: UsuarioService = Depends(get_service)):
    query = ObtenerUsuarioQuery(usuario_id)
    return service.obtener_usuario(query)

@app.get("/usuarios")
def listar_usuarios(service: UsuarioService = Depends(get_service)):
    return service.listar_usuarios()
