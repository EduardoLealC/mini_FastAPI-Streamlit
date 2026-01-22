from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

'''
    URL de conexión a la base de datos
    Usamos SQLite y el archivo se llamará "products.db"
    ./ es la carpeta raiz del proyecto
'''
DATABASE_URL = "sqlite:///./products.db"

''' 
    Creamos el engine (motor de conexión a la base de datos)
    El engine es el encargado de comunicarse con la BD
'''
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

'''
    Creamos una fábrica de sesiones
    Cada sesión permite hacer consultas, insertar, actualizar o borrar datos
'''
SessionLocal = sessionmaker(
    bind=engine, 
    autoflush=False, 
    autocommit=False
)


'''
    Clase base para todos los modelos (tablas)
    Todas las tablas deben heredar de esta clase
'''
class Base(DeclarativeBase):
    pass # No tiene código, solo sirve como base común
'''
Base:
Conecta clases con SQLAlchemy
Guarda metadata
Permite que el ORM funcione
'''