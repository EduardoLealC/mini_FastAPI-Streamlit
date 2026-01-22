import requests
from config import API_BASE_URL

def get_products():
    response = requests.get(API_BASE_URL)
    response.raise_for_status()
    return response.json()

def create_product(name: str, price: float):
    payload = {
        "name": name,
        "price": price
    }
    response = requests.post(API_BASE_URL, json=payload)
    response.raise_for_status()
    return response.json()
