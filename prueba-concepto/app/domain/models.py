# app/domain/models.py

from typing import Dict
from datetime import datetime


class ImagenMedica:
    ESTADOS_VALIDOS = ["subida", "anonimizada", "procesada", "disponible"]

    def __init__(
        self,
        id: str,
        tipo_imagen: str,
        region_anatomica: str,
        data: Dict,
        origen_datos: str,
        estado_procesamiento: str = "subida",
        fecha_subida: datetime = None,
    ):
        self.id = id
        self.tipo_imagen = tipo_imagen
        self.region_anatomica = region_anatomica
        self.data = data
        self.origen_datos = origen_datos
        self.estado_procesamiento = estado_procesamiento
        self.fecha_subida = fecha_subida or datetime.utcnow()
        self._validar()

    def _validar(self):
        if not self.id:
            raise ValueError("El ID de la imagen no puede estar vacío")
        if self.estado_procesamiento not in self.ESTADOS_VALIDOS:
            raise ValueError(f"Estado inválido: {self.estado_procesamiento}")