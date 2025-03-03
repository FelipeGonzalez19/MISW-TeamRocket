# app/domain/repositories.py


from abc import ABC, abstractmethod
from .models import ImagenMedica


class ImagenRepositorio(ABC):
    @abstractmethod
    def guardar(self, imagen: ImagenMedica):
        pass

    @abstractmethod
    def obtener_por_id(self, imagen_id: str):
        pass

    @abstractmethod
    def obtener_todas(self):
        pass
