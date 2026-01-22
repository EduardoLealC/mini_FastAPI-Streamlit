mini_fastAPI/
│
├── backend/                       # Backend con FastAPI (API REST)
│   ├── app/
│   │   ├── main.py                # Punto de entrada del backend (FastAPI)
│   │   │                          Crea la app - Registra routers - Inicializa la base de datos
│   │   │
│   │   ├── core/
│   │   │   └── database.py        # Configuración de la base de datos
│   │   │                          Engine SQLAlchemy - SessionLocal - Clase Base
│   │   │
│   │   ├── models/
│   │   │   └── product.py         # Modelo SQLAlchemy (tabla products)
│   │   │                          Define columnas y tipos - Representa la DB en Python
│   │   │
│   │   ├── schemas/
│   │   │   └── product.py         # Esquemas Pydantic
│   │   │                          Validación de datos de entrada - Serialización de respuestas
│   │   │
│   │   ├── services/
│   │   │   └── product_service.py # Lógica de negocio
│   │   │                          CRUD de productos - Interacción con la DB - Sin código FastAPI
│   │   │
│   │   └── api/
│   │       ├── router.py          # Router principal de la API
│   │       │                      Agrupa endpoints - Prefijo (/api)
│   │       │
│   │       └── endpoints/
│   │           └── products.py    # Endpoints REST de productos
│   │                              GET /products - POST /products
│   │
│   └── requirements.txt           # Dependencias del backend
│
├── frontend/                      # Frontend con Streamlit
│   │
│   ├── app.py                     # Página principal
│   │                             Configuración inicial y descripción
│   │
│   ├── pages/
│   │   ├── 1_Agregar.py           # Crear productos (POST)
│   │   └── 2_Listado.py           # Listar productos (GET)
│   │
│   ├── services/
│   │   └── api_client.py          # Cliente HTTP (requests)
│   │
│   ├── config.py                  # Configuración global
│   │
│   └── requirements.txt           # Dependencias del frontend
│
└── README.md                      # Documentación del proyecto
