# Aix – Gestor de Playlists

Este proyecto permite procesar playlists de YouTube para obtener las canciones y descargar las seleccionadas en formato ZIP.  
Consta de dos partes:  
- Backend: API REST en FastAPI.  
- Frontend: Interfaz en React (Vite) que consume la API y muestra las canciones.  

## Estructura del proyecto

```
aix/
│
├── backend/
│   ├── app/
│   │   ├── main.py          # Entrada de la API FastAPI
│   │   ├── routers/
│   │   │   └── playlist.py  # Endpoints para procesar playlists
│   │   └── ...              # Otros módulos
│   └── requirements.txt     # Dependencias del backend
│
├── frontend/
│   ├── index.html           # HTML base (con div#root)
│   ├── src/
│   │   ├── App.jsx          # Lógica de la interfaz
│   │   ├── App.css          # Estilos principales
│   │   ├── main.jsx         # Renderiza React en el root
│   │   └── services/
│   │       └── api.js       # Funciones para llamar al backend
│   └── package.json         # Dependencias del frontend
│
└── README.md                # Este archivo
```

## Backend (FastAPI)

### Requisitos
- Python 3.10+
- uvicorn como servidor ASGI  
- Dependencias del backend:

```bash
pip install -r requirements.txt
```

Ejemplo de requirements.txt:
```txt
fastapi
uvicorn
yt-dlp
pydantic
```

### Ejecutar backend

Desde la carpeta backend/:

```bash
uvicorn app.main:app --reload
```

El backend se ejecutará en:  
http://127.0.0.1:8000

### Endpoints principales

- GET `/playlists/parse?url=<playlist_url>`  
  Procesa una playlist de YouTube y devuelve las canciones.  

  Ejemplo respuesta:
  ```json
  {
    "songs": [
      {
        "title": "Canción 1",
        "url": "https://youtube.com/...",
        "artist": null,
        "album": null
      },
      {
        "title": "Canción 2",
        "url": "https://youtube.com/..."
      }
    ]
  }
  ```

- POST `/playlists/download`  
  Recibe una lista de URLs de canciones seleccionadas y genera un ZIP descargable.  

## Frontend (React + Vite)

### Requisitos
- Node.js 18+
- npm o yarn

### Ejecutar frontend

Desde la carpeta frontend/:

```bash
npm install
npm run dev
```

El frontend se ejecutará en:  
http://127.0.0.1:5173

### Funcionalidades

- Introducir la URL de una playlist de YouTube.  
- Ver la lista de canciones (solo títulos).  
- Seleccionar canciones con checkboxes.  
- Descargar seleccionadas en un ZIP.  

## Comunicación frontend-backend

- El frontend hace peticiones HTTP al backend FastAPI.  
- El backend debe estar corriendo en `http://127.0.0.1:8000`.  
- CORS está habilitado para permitir que el frontend (http://127.0.0.1:5173) consuma la API sin problemas.  
