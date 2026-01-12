# AIX

Aplicación simple de gestión de playlists, exportación entre plataformas, descarga, análisis de tracks individuales, búsqueda...

### Motivación
Crear un CRUD con FastAPI, SQLAlchemy, Postgres, Docker y demás para aprender más sobre el desarrollo con estas herramientas.

### Pasos a seguir

#### Modelado inicial de datos - definición de entidades:
- Playlist
- Track
- TrackInfo
- User

#### Organizar entorno Python
- Build venv
- Preparar docker-compose con postgres
- Instalar dependencias (poetry)
- Inicializar alembic
- Preparar configuración de la app (pydantic)

#### Definir ORM y crear migración de alembic
- Definir tablas con SQLAlchemy

#### Definir esquemas con Pydantic

#### Definir dependencias en FastAPI (Depends(get_db))

#### Implementar CRUD inicial para todas las entidades
- Create, Read, Update, Delete -> sin seguridad

#### Definir tests unitarios
- pytest

#### Implementar routes y definir mejor el API a exponer
- parse
- download
- import/export

#### Añadir módulo de usuarios

#### Añadir autenticación con JWT

#### Mejorar docker-compose
