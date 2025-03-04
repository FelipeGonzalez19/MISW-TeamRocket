#app/infrastructure/repositories.py


from sqlalchemy.orm import Session
from ..domain.models import ImagenMedica
from ..domain.repositories import ImagenRepositorio
from .models import ImagenMedicaDB

from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

class SQLAlchemyImagenRepositorio(ImagenRepositorio):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def guardar(self, imagen: ImagenMedica):
        db_imagen = self.obtener_por_id(imagen.id)
        if db_imagen:
            db_imagen.tipo_imagen = imagen.tipo_imagen
            db_imagen.region_anatomica = imagen.region_anatomica
            db_imagen.data = imagen.data
        else:
            db_imagen = ImagenMedicaDB(
                id=imagen.id,
                tipo_imagen=imagen.tipo_imagen,
                region_anatomica=imagen.region_anatomica,
                data=imagen.data
            )
            self.db_session.add(db_imagen)
        try:
            self.db_session.commit()
        except IntegrityError:
            self.db_session.rollback()
            raise HTTPException(status_code=400, detail="Error al guardar la imagen. ID posiblemente duplicado.")

    def obtener_por_id(self, imagen_id: str):
        return self.db_session.query(ImagenMedicaDB).filter(ImagenMedicaDB.id == imagen_id).first()

    def obtener_todas(self):
        return self.db_session.query(ImagenMedicaDB).all()
    
    def obtener_disponibles(self):
        return self.db_session.query(ImagenMedicaDB).filter(ImagenMedicaDB.estado_procesamiento == "disponible").all()