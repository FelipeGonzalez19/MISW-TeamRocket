# app/infrastructure/api.py

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from ...application.services import (
    ImagenCommandService,
    ImagenQueryService,
)
from ...application.commands import (
    ProcesarImagenCommand,
    RegistrarImagenCommand,
    ObtenerImagenQuery,
)
from ...domain.events import EventDispatcher
from .repositories import SQLAlchemyImagenRepositorio
from .database import get_db, init_db, Base, engine
from .models import ImagenInputDTO
from fastapi import HTTPException
from .despachadores import Despachador

init_db()

app = FastAPI()


def get_repo(db: Session = Depends(get_db)):
    return SQLAlchemyImagenRepositorio(db)


def get_event_dispatcher():
    return EventDispatcher()


def get_command_service(
    repo: SQLAlchemyImagenRepositorio = Depends(get_repo),
    dispatcher: EventDispatcher = Depends(get_event_dispatcher),
):
    return ImagenCommandService(repo, dispatcher)


def get_query_service(repo: SQLAlchemyImagenRepositorio = Depends(get_repo)):
    return ImagenQueryService(repo)


@app.get("/health")
def health_check():
    """Verifica si el servicio está funcionando correctamente."""
    return {"status": "ok", "message": "Servicio en funcionamiento"}


@app.post("/reset-db")
def reset_database():
    """OJO:BORRA TODO."""
    try:
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        return {"status": "success", "message": "Base de datos reseteada correctamente"}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al resetear la base de datos: {str(e)}"
        )


@app.post("/imagenes")
def registrar_imagen(
    imagen_data: ImagenInputDTO,
    service: ImagenCommandService = Depends(get_command_service),
):
    print("🔵 Recibido:", imagen_data.dict())
    try:
        command = RegistrarImagenCommand(imagen_data.dict())

        despachador = Despachador()
        despachador.publicar_comando(command, 'eventos-registrar-imagen')

        return service.registrar_imagen(command)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error interno del servidor: {str(e)}"
        )


@app.get("/imagenes/{imagen_id}")
def obtener_imagen(
    imagen_id: str, service: ImagenQueryService = Depends(get_query_service)
):
    query = ObtenerImagenQuery(imagen_id)
    return service.obtener_imagen(query)


@app.get("/imagenes")
def listar_imagenes(service: ImagenQueryService = Depends(get_query_service)):
    return service.listar_imagenes()


@app.post("/imagenes/procesar/{imagen_id}")
def procesar_imagen(
    imagen_id: str, service: ImagenCommandService = Depends(get_command_service)
):
    command = ProcesarImagenCommand(imagen_id)
    return service.procesar_imagen(command)
