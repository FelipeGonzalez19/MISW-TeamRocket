# app/domain/events.py

from typing import List, Callable, Dict, Type
import logging
from dataclasses import dataclass


class Event:
    pass


@dataclass
class ImagenAnonimizada:
    imagen_id: str


class ImagenRegistrada(Event):
    def __init__(self, imagen_id: str):
        self.imagen_id = imagen_id


class EventDispatcher:
    def __init__(self):
        self._handlers: Dict[Type[Event], List[Callable]] = {}

    def register(self, event_type: Type[Event], handler: Callable):
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)

    def dispatch(self, event: Event):
        for handler in self._handlers.get(type(event), []):
            handler(event)


logger = logging.getLogger(__name__)

dispatcher = EventDispatcher()
from .event_handlers import ImagenRegistradaHandler 

dispatcher.register(ImagenRegistrada, ImagenRegistradaHandler(logger).handle)
