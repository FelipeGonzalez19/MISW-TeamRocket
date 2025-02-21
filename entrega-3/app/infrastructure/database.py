# app/infrastructure/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
# en el .env el DATABASE_URL debe tener esta estructura
# DATABASE_URL=postgresql://usuario:contraseña@host:puerto/base_de_datos
# debe estar en el root de la entrega-3



engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def init_db():
    try:
        Base.metadata.create_all(bind=engine)
    except SQLAlchemyError as e:
        print(f"Error inicializando la BD: {e}")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
