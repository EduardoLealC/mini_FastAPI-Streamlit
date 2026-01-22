from fastapi import APIRouter
from app.api.endpoints import products

api_router = APIRouter(prefix="/api")

api_router.include_router(
    products.router,
    prefix="/products",
    tags=["Products"]
)
