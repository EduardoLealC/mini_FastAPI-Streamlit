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
│   │   │                           CRUD de productos - Interacción con la DB - No contiene código FastAPI
│   │   │
│   │   └── api/
│   │       ├── router.py          # Router principal de la API
│   │       │                      Agrupa todos los endpoints - Define prefijos (/api)
│   │       │
│   │       └── endpoints/
│   │           └── products.py    # Endpoints REST de productos
│   │                              GET /products - POST /products - Maneja requests y responses
│   │
│   └── requirements.txt           # Dependencias del backend
│
├── frontend/                      # Frontend con Streamlit
│   │
│   ├── app.py                    # Página principal (Home)
│   │                             Configuración inicial de Streamlit - Descripción de la aplicación
│   │
│   ├── pages/
│   │   ├── 1_Agregar.py          # Página para crear productos
│   │   │                         Formulario - Llama al backend (POST)
│   │   │
│   │   └── 2_Listado.py          # Página para listar productos
│   │                             Llama al backend (GET) - Muestra tabla y métricas
│   │
│   ├── services/
│   │   └── api_client.py         # Cliente HTTP del frontend
│   │                             Usa requests - Encapsula llamadas a la API - No contiene lógica de UI
│   │
│   ├── config.py                 # Configuración del frontend
│   │                             URL del backend - Constantes globales
│   │
│   └── requirements.txt          # Dependencias del frontend
│
└── README.md                     # Documentación del proyecto
                                 # Explica arquitectura, flujo y uso
