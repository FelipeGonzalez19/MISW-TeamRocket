# STA - Servicio de Procesamiento de Imágenes Médicas

## Descripción del Proyecto

Este servicio forma parte del ecosistema de **SaludTech de los Alpes (STA)** y está diseñado para la gestión y procesamiento de imágenes médicas de forma segura y eficiente. Implementa los principios de **DDD (Domain-Driven Design)** y una **arquitectura hexagonal** basada en **eventos de dominio** para garantizar modularidad y escalabilidad.

---

## Arquitectura y Principios de Diseño

El servicio sigue una **arquitectura basada en eventos** y principios de **DDD**. Algunos de los conceptos clave implementados incluyen:

- **Entidades y Objetos de Valor**:  
  La imagen médica es una entidad central con atributos como `tipo_imagen`, `region_anatomica` y `estado_procesamiento`.

- **Agregados**:  
  La imagen médica y su estado de procesamiento conforman un agregado.

- **Patrón CQS (Command Query Separation)**:  
  Se separan los comandos para modificar el estado del sistema de las consultas para obtener información.

- **Eventos de Dominio**:  
  Se utilizan eventos como `ImagenRegistrada` e `ImagenAnonimizada` para comunicar cambios entre módulos.

- **Persistencia con Base de Datos Relacional**:  
  Se usa **SQLAlchemy** para la persistencia en una base de datos real.

- **Arquitectura Hexagonal**:  
  Se implementan **puertos y adaptadores** para desacoplar la lógica de negocio de la infraestructura.

---

## Estructura Carpetas

## 📂 `application/` - Capa de Aplicación

Esta capa contiene la lógica de **casos de uso** y **servicios de aplicación**.

- **`commands.py`**: Define los comandos (acciones) que la aplicación puede ejecutar.

  - `ProcesarImagenCommand`: Comando para anonimizar una imagen.
  - `RegistrarImagenCommand`: Comando para registrar una imagen en el sistema.
  - `ObtenerImagenQuery`: Consulta para obtener una imagen por ID.

- **`services.py`**: Contiene la lógica de los servicios de aplicación.
  - `ImagenCommandService`: Maneja comandos de creación y procesamiento de imágenes.
  - `ImagenQueryService`: Proporciona métodos para consultar imágenes.

---

## 📂 `domain/` - Capa de Dominio

Define las entidades, eventos de dominio y reglas de negocio.

- **`models.py`**: Define la entidad `ImagenMedica` con sus atributos y validaciones.
- **`events.py`**: Define los eventos de dominio, como `ImagenRegistrada` e `ImagenAnonimizada`.
- **`event_handlers.py`**: Contiene manejadores de eventos que ejecutan acciones cuando ocurren eventos de dominio.
- **`repositories.py`**: Define la interfaz `ImagenRepositorio`, asegurando una abstracción sobre los datos.

---

## 📂 `infrastructure/` - Capa de Infraestructura

Contiene la implementación de repositorios, la API y la conexión con la base de datos.

- **`api.py`**: Define los endpoints de FastAPI y la inyección de dependencias.
- **`database.py`**: Configura la base de datos PostgreSQL con SQLAlchemy.
- **`models.py`**: Define el modelo de base de datos `ImagenMedicaDB`.
- **`repositories.py`**: Implementa `SQLAlchemyImagenRepositorio` para interactuar con la base de datos.

---

## 📂 `main.py`

Archivo principal que inicia la aplicación FastAPI.

---

## 📂 `locustfile.py`

Archivo para las pruebas de carga y estres. Test de rendimiento de la aplicacion.

---

## 🔗 Flujo de Trabajo

1. **Un cliente envía una solicitud** para registrar una imagen (`POST /imagenes`).
2. **El servicio de aplicación** recibe la solicitud y ejecuta el comando `RegistrarImagenCommand`.
3. **El dominio valida los datos** y crea una entidad `ImagenMedica`.
4. **El repositorio guarda la imagen** en la base de datos.
5. **Se dispara un evento de dominio** (`ImagenRegistrada`).
6. **El manejador de eventos** procesa la acción (ej. logs, notificaciones, etc.).
7. **El cliente puede consultar las imágenes** (`GET /imagenes` o `GET /imagenes/{imagen_id}`).

Esta arquitectura permite **modularidad**, **separación de responsabilidades** y **fácil integración con nuevas tecnologías**.

---

## Módulos del Servicio

El servicio está compuesto por los siguientes módulos:

### 1. Módulo de Aplicación

Encapsula la lógica de negocio a través de comandos, consultas y servicios de aplicación:

- **Comandos**:

  - `RegistrarImagenCommand`
  - `ProcesarImagenCommand`

- **Consultas**:

  - `ObtenerImagenQuery`

- **Servicios**:
  - `ImagenCommandService`
  - `ImagenQueryService`

### 2. Módulo de Dominio

Define las reglas de negocio y los eventos de dominio:

- **Entidades**:

  - `ImagenMedica`

- **Eventos**:

  - `ImagenRegistrada`
  - `ImagenAnonimizada`

- **Manejadores de Eventos**:

  - `ImagenRegistradaHandler`

- **Repositorio Abstracto**:
  - `ImagenRepositorio`

### 3. Módulo de Infraestructura

Proporciona implementaciones concretas para la persistencia y la API:

- **Base de Datos**:  
  Implementada con **SQLAlchemy**.

- **Repositorio Concreto**:  
  `SQLAlchemyImagenRepositorio`

- **API REST**:  
  Implementada con **FastAPI**.

---

## Escenarios de Calidad

El sistema se ha diseñado considerando los siguientes atributos de **rendimiento**:

- **Baja latencia**:  
  Se optimizan las consultas y el procesamiento para minimizar los tiempos de respuesta.

- **Alta concurrencia**:  
  Se soporta el procesamiento simultáneo de múltiples imágenes sin afectar el rendimiento.

- **Eficiencia en el uso de recursos**:  
  Se implementan estrategias de almacenamiento y procesamiento optimizadas para manejar grandes volúmenes de datos sin degradar el sistema.

---

## Requisitos de Instalación y Ejecución

### Prerrequisitos

- Python 3.8+
- fastapi
- uvicorn
- sqlalchemy
- psycopg2-binary
- pydantic
- python-dotenv
- psycopg2
- locust
- Base de datos PostgreSQL u otra base de datos relacional compatible

### Instalación

```sh
pip install -r requirements.txt
```

### Ejecución del Servicio

```sh
uvicorn app.infrastructure.api:app --host 0.0.0.0 --port 8000
```

### Endpoints disponibles

| Método | Endpoint                  | Descripción                                      |
| ------ | ------------------------- | ------------------------------------------------ |
| GET    | `/health`                 | Verifica el estado del servicio                  |
| POST   | `/imagenes`               | Registra una nueva imagen médica                 |
| POST   | `/imagenes/{id}/procesar` | Inicia el proceso de anonimización de una imagen |
| GET    | `/imagenes/{id}`          | Obtiene una imagen por su ID                     |
| GET    | `/imagenes`               | Lista todas las imágenes registradas             |

### Documentación de la API

### Verificar estado del servicio

**Endpoint:** `/health`  
**Método:** `GET`  
**Descripción:** Verifica si el servicio está funcionando correctamente.  
**Respuesta:**

```json
{
  "status": "ok",
  "message": "Servicio en funcionamiento"
}
```

### Resetear la base de datos

**Endpoint:** `/reset-db`  
**Método:** `POST`  
**Descripción:** Borra y recrea la base de datos.
**Respuesta:**

```json
{
  "status": "success",
  "message": "Base de datos reseteada correctamente"
}
```

### Registrar una imagen

**Endpoint:** `/imagenes`  
**Método:** `POST`  
**Descripción:** Registra una nueva imagen en el sistema.
**Informacion enviada:**

```json
{
  "id": "1",
  "tipo_imagen": "Rayos X",
  "region_anatomica": "Torax",
  "origen_datos": "Torax",
  "data": {
    "resolucion": "1024x768",
    "formato": "DICOM"
  }
}
```

**Respuesta:**

```json
{
  "id": "1",
  "tipo_imagen": "Rayos X",
  "region_anatomica": "Torax",
  "data": {
    "resolucion": "1024x768",
    "formato": "DICOM"
  },
  "origen_datos": "Torax",
  "estado_procesamiento": "subida",
  "fecha_subida": "2025-02-21T14:53:22.335264"
}
```

### Obtener una imagen por ID

**Endpoint:** `/imagenes/{imagen_id}`  
**Método:** `GET`  
**Descripción:** Obtiene los datos de una imagen por su ID.
**Respuesta:**

```json
{
  "tipo_imagen": "Rayos X",
  "id": "fddsdsg",
  "region_anatomica": "Torax"
}
```

### Obtener una imagen por ID

**Endpoint:** `/imagenes/{imagen_id}`  
**Método:** `GET`  
**Descripción:** Retorna una lista de todas las imágenes registradas.
**Respuesta:**

```json
{
    {
        "tipo_imagen": "Rayos X",
        "id": "fddsdsg",
        "region_anatomica": "Torax"
    }
}
```

### Procesar una imagen

**Endpoint:** `/imagenes/procesar/{imagen_id}`  
**Método:** `POST`  
**Descripción:** Procesa una imagen existente en el sistema.
**Respuesta:**

```json
{
  "mensaje": "Imagen en proceso de anonimización"
}
```

# Pasos para ejecutar la aplicación

## 1. Clonar el repositorio

```bash


```

## 2. Crear y activar un entorno virtual

```bash
python -m venv venv   #mac
source venv/bin/activate  #windows

```

## 3. Instalar dependencias

```bash
pip install -r requirements.txt

```

## 4. Configurar variables de entorno

```bash
DATABASE_URL=postgresql://sta_user:password@localhost/sta_db

```

## 5. Inicializar la base de datos

```bash
python -m app.infrastructure.database
```

## 6. Ejecutar la aplicación

```bash
uvicorn app.infrastructure.api:app --host 0.0.0.0 --port 8000 --reload
```
