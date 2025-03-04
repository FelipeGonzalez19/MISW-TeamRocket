# app/application/services.py
from fastapi import HTTPException
from ..domain.models import ImagenMedica
from ..infrastructure.Imagenes.repositories import ImagenRepositorio
from ..infrastructure.Anonimizar.repositories import AnonimizacionRepositorio
from ..domain.events import EventDispatcher, ImagenAnonimizada, ImagenRegistrada
from .commands import ObtenerImagenQuery, ProcesarImagenCommand, RegistrarImagenCommand, AnonimizarImagenCommand


class ImagenCommandService:
    def __init__(self, repo: ImagenRepositorio, event_dispatcher: EventDispatcher):
        self.repo = repo
        self.event_dispatcher = event_dispatcher

    def registrar_imagen(self, command: RegistrarImagenCommand):
        imagen = ImagenMedica(**command.imagen_data)
        self.repo.guardar(imagen)
        self.event_dispatcher.dispatch(ImagenRegistrada(imagen.id))
        return imagen

    def __init__(self, repo: ImagenRepositorio, event_dispatcher: EventDispatcher):
        self.repo = repo
        self.event_dispatcher = event_dispatcher

    def procesar_imagen(self, command: ProcesarImagenCommand):
        imagen = self.repo.obtener_por_id(command.id)
        if not imagen:
            raise HTTPException(status_code=404, detail="Imagen no encontrada")

        imagen.estado_procesamiento = "anonimizada"
        self.repo.guardar(imagen)

        self.event_dispatcher.dispatch(ImagenAnonimizada(imagen.id))
        return {"mensaje": "Imagen en proceso de anonimización"}


class ImagenQueryService:
    def __init__(self, repo: ImagenRepositorio):
        self.repo = repo

    def obtener_imagen(self, query: ObtenerImagenQuery):
        return self.repo.obtener_por_id(query.imagen_id)

    def listar_imagenes(self):
        return self.repo.obtener_todas()
    
class AnonimizacionService:
    def __init__(self, repo: AnonimizacionRepositorio):
        self.repo = repo

    def anonimizar_imagen(self, command: AnonimizarImagenCommand):
        registro = self.repo.obtener_por_id(command.imagen_id)
        if not registro:
            raise HTTPException(status_code=404, detail="Imagen no encontrada")

        registro.estado = "anonimizado"
        self.repo.guardar(registro)

        return ImagenAnonimizada(command.imagen_id)
