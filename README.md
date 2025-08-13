# Aix – Music Manager con FastAPI

## Resumen general

**Nombre provisional:** Aix  
**Objetivo principal:**
- Gestionar playlists locales (carpetas en disco, incluidas unidades externas como USBs).
- Integrar extracción de información y descarga masiva desde servicios externos como SoundCloud, Spotify, etc.
- Permitir mover canciones entre playlists con opción de revertir cambios.
- Consultar playlists y canciones vía API.

**Arquitectura actual:**
- **Backend:** FastAPI + SQLModel (SQLite como base inicial).
- **Frontend:** React + Vite (previsto para futuro, no prioritario ahora).
- **Persistencia:** SQLite con SQLModel y migraciones manuales.
- **Autenticación:** Basada en lógica heredada de Flask, pendiente de migrar a FastAPI.
- **Ejecución:**  
  ```bash
  fastapi dev app/main.py
  ```

---

## Estructura de carpetas

```
aix/
│
├── app/
│   ├── __init__.py
│   ├── main.py              # Punto de entrada
│   ├── db.py                # Configuración BD
│   ├── models.py            # Entidades SQLModel/Pydantic
│   ├── routers/             # Endpoints por módulo
│   │   ├── __init__.py
│   │   ├── playlist.py
│   │   ├── song.py          # Pendiente
│   │   ├── auth.py          # Pendiente
│   ├── services/            # Lógica de negocio
│   │   ├── __init__.py
│   │   ├── local_playlists.py
│   │   ├── soundcloud.py    # Pendiente
│   │   ├── spotify.py       # Pendiente
│
├── .venv/
├── requirements.txt
└── README.md
```

---

## Modelo de datos actual

```python
from datetime import datetime
from sqlmodel import SQLModel, Field

class Playlist(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    created: datetime = Field(default_factory=datetime.utcnow)
    author_id: int
```

- Próxima adición: `Song` (relacionada con `Playlist`).
- Futura entidad: `User` (para asociar playlists a usuarios).

---

## Estado actual

✅ Arranque con `fastapi dev app/main.py`  
✅ Endpoint `/playlists/` funcionando y consultando BD  
✅ Base de datos SQLite inicializada con SQLModel  
⚠ Sin datos de prueba insertados  
⚠ Autenticación pendiente  
⚠ CRUD incompleto para playlists  
⚠ Lógica de manejo de playlists locales y externas no implementada  

---

## Pasos recientes

- Migración de Flask → FastAPI con estructura modular (`routers` + `services`).
- Sustitución de SQL manual por ORM SQLModel.
- Estructura mínima de carpetas para escalabilidad.
- Conexión y consulta inicial con SQLAlchemy/SQLModel.
- Corrección de error *"no such table"* inicializando la BD antes del arranque.

---

## Próximos pasos

1. Añadir CRUD completo de playlists (GET, POST, PUT, DELETE).
2. Insertar datos de prueba para validar endpoints.
3. Implementar `local_playlists.py` para:
   - Escanear carpetas locales como playlists.
   - Listar canciones en cada playlist.
   - Mover canciones entre playlists.
   - Registrar cambios para revertir operaciones.
4. Diseñar integración inicial con SoundCloud.
5. Migrar autenticación a FastAPI con JWT/OAuth2.
6. Preparar API para React + Vite cuando el backend sea estable.

---

## Consideraciones técnicas

- **Entorno virtual:** usar `.venv` por proyecto para aislar dependencias.
- **Base de datos:** SQLite para prototipos, posible migración a PostgreSQL.
- **Ejecución:** `fastapi dev` para aprovechar *autoreload*.
- **Modelado:** SQLModel combina Pydantic + SQLAlchemy.
- **Frontend:** previsto, pero no prioritario.

---

## Peculiaridades de implementación

- **Migración de Flask a FastAPI:**  
  Estructura modular adaptada de *Blueprints* a *routers*.
- **Objetivo mixto local/online:**  
  Gestión de playlists tanto en BD como en sistema de archivos.
- **Servicios externos:**  
  Integraciones previstas con SoundCloud y Spotify.
- **Diseño modular:**  
  `services/` para lógica de negocio, `routers/` para endpoints.
- **Persistencia híbrida:**  
  Playlists en BD, música en sistema de archivos o API externa.
- **Ejecución en desarrollo:**  
  Imports corregidos asegurando `__init__.py` en `app/`.

---

## Avances recientes
- Conversión completa de Flask → FastAPI con routers.
- BD inicializada automáticamente en `init_db()`.
- Uso de `routers/playlist.py` para rutas de playlists.
- Preparación de `routers/sync.py` para sincronizar música local/remota.
- Diseño para aceptar ruta personalizada en POST `/sync`.
- Plan de análisis superficial con `mutagen` y profundo con Essentia.
- Futuro soporte para procesamiento concurrente con Celery o RQ.

---

## Próximos pasos inmediatos
1. Crear `config.py` con `DEFAULT_MUSIC_PATH`.
2. Implementar `sync_service.py` para análisis y registro en BD.
3. Añadir `routers/sync.py` con endpoint POST `/sync`.
4. Probar análisis superficial con `mutagen`.
5. Planificar integración con Celery/RQ.
