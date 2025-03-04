from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from ...application.services import AnonimizacionService
from ...application.commands import AnonimizarImagenCommand
from .repositories import AnonimizacionRepositorio
from .database import get_db

app = FastAPI()

def get_repo(db: Session = Depends(get_db)):
    return AnonimizacionRepositorio(db)

def get_service(repo: AnonimizacionRepositorio = Depends(get_repo)):
    return AnonimizacionService(repo)

@app.post("/anonimizar/{imagen_id}")
def anonimizar_imagen(imagen_id: str, service: AnonimizacionService = Depends(get_service)):
    command = AnonimizarImagenCommand(imagen_id)
    return service.anonimizar_imagen(command)