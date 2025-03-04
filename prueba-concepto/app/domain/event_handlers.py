# app/domain/event_handlers.py

import logging
from ..domain.events import ImagenRegistrada, ImagenAnonimizada, UsuarioRegistrado

logger = logging.getLogger(__name__)


class ImagenRegistradaHandler:
    def __init__(self, logger):
        self.logger = logger

    def handle(self, event: ImagenRegistrada):
        self.logger.info(f"🖼️ Imagen registrada con ID: {event.imagen_id}")
        
class ImagenAnonimizadaHandler:
    def __init__(self, logger):
        self.logger = logger

    def handle(self, event: ImagenAnonimizada):
        self.logger.info(f"🔒 Imagen anonimizada con ID: {event.imagen_id}")

class UsuarioRegistradoHandler:
    def __init__(self, logger):
        self.logger = logger

    def handle(self, event: UsuarioRegistrado):
        self.logger.info(f"✅ Usuario registrado con ID: {event.usuario_id}")
