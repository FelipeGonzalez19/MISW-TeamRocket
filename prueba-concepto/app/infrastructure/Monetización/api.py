from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from ...application.services import MonetizacionService
from ...application.commands import RegistrarAccesoImagenCommand
from ..Monetización.repositories import MonetizacionRepositorio
from ..Monetización.database import get_db

app = FastAPI()

def get_repo(db: Session = Depends(get_db)):
    return MonetizacionRepositorio(db)

def get_service(repo: MonetizacionRepositorio = Depends(get_repo)):
    return MonetizacionService(repo)

@app.post("/monetizacion/acceso")
def registrar_acceso(imagen_id: str, usuario_id: str, service: MonetizacionService = Depends(get_service)):
    command = RegistrarAccesoImagenCommand(imagen_id, usuario_id)
    return service.registrar_acceso(command)

@app.get("/monetizacion")
def listar_monetizaciones(service: MonetizacionService = Depends(get_service)):
    return service.repo.obtener_todos()
