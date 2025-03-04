# app/domain/event_handlers.py

import logging
from ..domain.events import ImagenRegistrada, ImagenAnonimizada, UsuarioRegistrado, ImagenAccedida

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

class ImagenAccedidaHandler:
    def __init__(self, logger):
        self.logger = logger

    def handle(self, event: ImagenAccedida):
        self.logger.info(f"💰 Acceso registrado para imagen {event.imagen_id} por usuario {event.usuario_id}")
