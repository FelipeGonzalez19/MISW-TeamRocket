# app/application/commands.py

class ProcesarImagenCommand:
    def __init__(self, id: str):
        self.id = id


class RegistrarImagenCommand:
    def __init__(self, imagen_data: dict):
        self.imagen_data = imagen_data


class ObtenerImagenQuery:
    def __init__(self, imagen_id: str):
        self.imagen_id = imagen_id

class AnonimizarImagenCommand:
    def __init__(self, imagen_id: str):
        self.imagen_id = imagen_id
        
class RegistrarUsuarioCommand:
    def __init__(self, usuario_data: dict):
        self.usuario_data = usuario_data

class ObtenerUsuarioQuery:
    def __init__(self, usuario_id: str):
        self.usuario_id = usuario_id