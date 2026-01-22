## Descripición general
Este proyecto es una aplicación full-stack mínima diseñada para demostrar una arquitectura clara y desacoplada entre frontend y backend.

Permite:

- Crear productos (nombre y precio)
- Listar productos almacenados
-  Visualizar un pequeño resumen desde el frontend

El objetivo principal no es la UI, sino mostrar una separación correcta de responsabilidades y un flujo limpio de datos.

## Cómo ejecutar el proyecto
**Backend**:
- pip install -r requirements.txt
- uvicorn app.main:app --reload

__Frontend__:
- pip install -r requirements.txt
- streamlit run app.py

## Arquitectura

La aplicación está dividida en dos capas independientes:

- __Backend (FastAPI)__:
Responsable de la lógica de negocio, validación y persistencia de datos.

- __Frontend (Streamlit)__:
Responsable únicamente de la interacción con el usuario y el consumo de la API.

Reglas de diseño
- El frontend NO accede directamente a la base de datos
- Toda la lógica y persistencia pasan por FastAPI
- Streamlit actúa solo como cliente de la API REST
- Cada capa puede evolucionar de forma independiente

## Backend - FastAPI
__Responsabilidades__:
- Exponer endpoints REST (GET, POST)
- Validar datos de entrada y salida con Pydantic
- Gestionar la lógica de negocio
- Persistir datos en SQLite mediante SQLAlchemy

__Flujo interno:__
```text
Request HTTP
   ↓
Endpoint (FastAPI)
   ↓
Schema Pydantic (validación)
   ↓
Service (lógica de negocio)
   ↓
Modelo SQLAlchemy
   ↓
Base de datos (SQLite)
```

## Frontend - Streamlit
__Responsabilidades__:

- Proveer una interfaz simple para el usuario
- Enviar solicitudes HTTP al backend
- Mostrar datos y métricas obtenidas desde la API

```text
Usuario
   ↓
Streamlit UI
   ↓
API Client (requests)
   ↓
Backend FastAPI
```




## Estructura del proyecto

```text
mini_fastAPI/
│
├── backend/                       # Backend con FastAPI (API REST)
│   ├── app/
│   │   ├── main.py                # Punto de entrada del backend (FastAPI)
│   │   │                          Crea la app, registra routers e inicializa la DB
│   │   │
│   │   ├── core/
│   │   │   └── database.py        # Configuración de la base de datos
│   │   │                          Engine SQLAlchemy, SessionLocal, Base
│   │   │
│   │   ├── models/
│   │   │   └── product.py         # Modelo SQLAlchemy (tabla products)
│   │   │
│   │   ├── schemas/
│   │   │   └── product.py         # Esquemas Pydantic
│   │   │
│   │   ├── services/
│   │   │   └── product_service.py # Lógica de negocio (CRUD)
│   │   │
│   │   └── api/
│   │       ├── router.py          # Router principal (/api)
│   │       └── endpoints/
│   │           └── products.py    # Endpoints REST
│   │
│   └── requirements.txt           # Dependencias del backend
│
├── frontend/                      # Frontend con Streamlit
│   ├── app.py                     # Página principal
│   ├── pages/
│   │   ├── 1_Agregar.py           # Crear productos
│   │   └── 2_Listado.py           # Listar productos
│   │
│   ├── services/
│   │   └── api_client.py          # Cliente HTTP
│   │
│   ├── config.py                  # Configuración global
│   └── requirements.txt           # Dependencias del frontend
│
└── README.md                      # Documentación del proyecto
```