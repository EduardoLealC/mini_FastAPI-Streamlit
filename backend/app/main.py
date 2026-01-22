from fastapi import FastAPI
from app.api.router import api_router 
from app.core.database import Base, engine

# Se crea la instancia de FastAPI
app = FastAPI(title="Mini Fullstack API") 

# Inicializa la base de datos (import app.core.database)
Base.metadata.create_all(bind=engine) 

#Registra las rutas del API (import app.api.router)
app.include_router(api_router) 
