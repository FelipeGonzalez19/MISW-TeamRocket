# STA - Plataforma de Procesamiento de Imágenes Médicas

## Descripción del Proyecto

Este sistema forma parte del ecosistema de **SaludTech de los Alpes (STA)** y está diseñado para la gestión y procesamiento de imágenes médicas de manera segura y eficiente. Implementa los principios de **DDD (Domain-Driven Design)** y una **arquitectura hexagonal** basada en **eventos de dominio** para garantizar modularidad, escalabilidad y desacoplamiento.

## Arquitectura y Principios de Diseño

El sistema sigue una **arquitectura basada en eventos** y principios de **DDD**. Se implementan los siguientes conceptos:

- **Entidades y Objetos de Valor**  
  - Se definen entidades clave como `ImagenMedica`, `Usuario`, `RegistroAnonimizacion` y `TransaccionMonetizacion`.

- **Agregados**  
  - Cada entidad gestiona su propio estado y se organiza en agregados dentro del dominio.

- **Patrón CQS (Command Query Separation)**  
  - Se separan los comandos, que modifican el estado del sistema, de las consultas, que solo leen información.

- **Eventos de Dominio**  
  - Se utilizan eventos como `ImagenRegistrada`, `ImagenAnonimizada`, `UsuarioRegistrado` y `PagoProcesado` para comunicar cambios entre módulos.

- **Persistencia con Base de Datos Relacional**  
  - Se utiliza **SQLAlchemy** para la gestión de la persistencia en bases de datos PostgreSQL.

- **Arquitectura Hexagonal**  
  - Se implementan **puertos y adaptadores** para desacoplar la lógica de negocio de la infraestructura.

## Microservicios Implementados

El sistema se compone de **cuatro microservicios**, cada uno con una responsabilidad específica:

1. **Microservicio de Imágenes**  
   - Permite la carga y almacenamiento de imágenes médicas.
   - Expone API REST para registrar y consultar imágenes.
   - Genera eventos cuando una imagen es subida.

2. **Microservicio de Anonimización**  
   - Procesa imágenes médicas para anonimizar datos sensibles.
   - Dispara eventos cuando la anonimización se ha completado.

3. **Microservicio de Usuarios**  
   - Registra y gestiona la información de los usuarios del sistema.
   - Mantiene un registro de intentos de inicio de sesión.
   - Permite la consulta de información de los usuarios.

4. **Microservicio de Monetización**  
   - Gestiona pagos y cobros a proveedores de imágenes.
   - Lleva el control de transacciones basadas en el uso de imágenes anonimizadas.

## Flujo de Trabajo

1. Un usuario **sube una imagen médica** mediante `POST /imagenes`.
2. El microservicio de imágenes **almacena la imagen** y emite el evento `ImagenRegistrada`.
3. El microservicio de anonimización **escucha el evento y anonimiza la imagen**.
4. Una vez anonimizada, el sistema **genera el evento `ImagenAnonimizada`**.
5. Cuando otro usuario **solicita la imagen anonimizada**, el sistema **genera un evento de uso de datos** (`EventoUsoDatos`).
6. **El microservicio de monetización procesa la transacción** y calcula el monto adeudado al proveedor de la imagen.

## Endpoints Disponibles

| Microservicio    | Método  | Endpoint                         | Descripción                                      |
|-----------------|---------|---------------------------------|--------------------------------------------------|
| Imágenes        | `POST`  | `/imagenes`                     | Registra una nueva imagen médica.               |
|                 | `GET`   | `/imagenes/{imagen_id}`         | Obtiene los detalles de una imagen por ID.      |
|                 | `GET`   | `/imagenes`                     | Lista todas las imágenes registradas.           |
| Anonimización   | `POST`  | `/anonimizar/{imagen_id}`       | Inicia el proceso de anonimización de una imagen. |
| Usuarios        | `POST`  | `/usuarios`                     | Registra un nuevo usuario.                      |
|                 | `GET`   | `/usuarios/{usuario_id}`        | Obtiene la información de un usuario.          |
|                 | `GET`   | `/usuarios`                     | Lista todos los usuarios registrados.          |
| Monetización    | `POST`  | `/monetizacion/pagar`           | Procesa un pago por uso de imágenes.           |
|                 | `GET`   | `/monetizacion/saldo/{usuario_id}` | Consulta el saldo acumulado de un usuario. |

## Instalación y Ejecución

### Prerrequisitos

- Python 3.8+
- FastAPI
- Uvicorn
- SQLAlchemy
- Psycopg2-binary
- Pydantic
- Python-dotenv
- Locust
- PostgreSQL

### Instalación de Dependencias

pip install -r requirements.txt

### Ejecución del Servicio

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

### Pruebas de Carga con Locust
Para ejecutar pruebas de rendimiento con Locust:

locust -f locustfile.py --host=http://0.0.0.0:8000

### Accede a la interfaz de Locust en:
http://localhost:8089

### Variables de Entorno
El sistema requiere las siguientes variables de entorno configuradas en un archivo .env:

DATABASE_URL_IMAGENES=postgresql://user:password@localhost/imagenes_db
DATABASE_URL_ANONIMIZACION=postgresql://user:password@localhost/anonimizacion_db
DATABASE_URL_USUARIOS=postgresql://user:password@localhost/usuarios_db
DATABASE_URL_MONETIZACION=postgresql://user:password@localhost/monetizacion_db

### Estructura de la Base de Datos
Cada microservicio mantiene su propia base de datos con las siguientes estructuras:

1. Base de datos de imágenes:
  
  `CREATE TABLE imagenes (
      id VARCHAR PRIMARY KEY,
      tipo_imagen VARCHAR NOT NULL,
      region_anatomica VARCHAR NOT NULL,
      data JSON NOT NULL
  );`

2. Base de datos de anonimización:

  `CREATE TABLE anonimizar (
      id VARCHAR PRIMARY KEY,
      imagen_id VARCHAR NOT NULL,
      estado VARCHAR NOT NULL DEFAULT 'pendiente'
  );`

3. Base de datos de usuarios:

  `CREATE TABLE usuarios (
      id VARCHAR PRIMARY KEY,
      nombre VARCHAR NOT NULL,
      email VARCHAR UNIQUE NOT NULL,
      intentos_login INT DEFAULT 0
  );`
4. Base de datos de monetización:

  `CREATE TABLE monetizacion (
      id VARCHAR PRIMARY KEY,
      usuario_id VARCHAR NOT NULL,
      saldo_pendiente FLOAT DEFAULT 0
  );`
