import pulsar
from pulsar.schema import *
import utils

from ...application.commands import (
    ProcesarImagenCommand,
)

class Despachador:
    def __init__(self):
        pass

    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        #payload = ComandoCrearReservaPayload(
        #    id_usuario=str(comando.id_usuario)
        #    # agregar itinerarios
        #)
        comando_integracion = ProcesarImagenCommand(id=comando.id)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ProcesarImagenCommand))
