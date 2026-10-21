import os
import httpx

PRODUCT_SERVICE_URL = os.getenv(
    "PRODUCT_SERVICE_URL", "http://127.0.0.1:8001"
)

def fetch_product(product_id: int) -> dict:
    response = httpx.get(
        f"{PRODUCT_SERVICE_URL}/products/{product_id}",
        timeout=3.0,
    )
    response.raise_for_status()
    return response.json()

def get_product_fetcher():
    return fetch_product

def fetch_products() -> list[dict]:
    response = httpx.get(
        "{PRODUCT_SERVICE_URL}/products",
        timeout=3.0,
    )
    response.raise_for_status()
    return response.json()

def get_products_fetcher():
    return fetch_products ## Task C mentions "returns fetch_product (without calling it)", research and clarify this without calling it part



