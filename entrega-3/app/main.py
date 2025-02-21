# app/main.py

from fastapi import FastAPI, Request
import time
import logging

from .domain.events import dispatcher  


def get_event_dispatcher():
    return dispatcher 


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.middleware("http")
async def medir_tiempo_middleware(request: Request, call_next):
    inicio = time.time()
    response = await call_next(request)
    duracion = time.time() - inicio
    logger.info(
        f"Tiempo de ejecución para {request.method} {request.url.path}: {duracion:.4f} segundos"
    )
    return response
