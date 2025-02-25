# app/domain/event_handlers.py

import logging
from ..domain.events import ImagenRegistrada

logger = logging.getLogger(__name__)


class ImagenRegistradaHandler:
    def __init__(self, logger):
        self.logger = logger

    def handle(self, event: ImagenRegistrada):
        self.logger.info(f"🖼️ Imagen registrada con ID: {event.imagen_id}")
