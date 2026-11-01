import httpx
from app.main import app
from app.product_client import get_product_fetcher, get_products_fetcher

PRODUCTS=[
    {"id": 1, "name": "Laptop", "price": 899.00},
    {"id": 2, "name": "Mouse", "price": 25.0},
]

def fake_fetch_product(product_id: int) -> dict:
    return {"id": product_id, "name": "Laptop", "price": 899.00}

def provide_fake_product():
    return fake_fetch_product 

def fake_fetch_products() -> list[dict]:
    return PRODUCTS

def provide_fake_products():
    return fake_fetch_products

def test_remote_products_success(client):
    app.dependency_overrides[get_products_fetcher] = provide_fake_products
    try:
        response = client.get("/api/products")
        assert response.status_code == 200
        assert response.json() == PRODUCTS
        assert len(response.json()) == 2
    finally: 
        app.dependency_overrides.pop(get_products_fetcher, None)


def test_remote_product_success(client):
    app.dependency_overrides[get_product_fetcher] = provide_fake_product
    try:
        response = client.get("/api/products/1")
        assert response.status_code == 200
        assert response.json()["name"] == "Laptop"
    finally: 
        app.dependency_overrides.pop(get_product_fetcher, None)

def fake_product_missing(product_id: int):
    request = httpx.Request(
        "GET", f"http://example.test/products/{product_id}"
    )
    response = httpx.Response(404, request=request)
    raise httpx.HTTPStatusError(
        "Not found", request=request, response=response
    )

def provide_missing_product():
    return fake_product_missing

def test_remote_product_missing(client):
    app.dependency_overrides[get_product_fetcher] = provide_missing_product
    try:
        response = client.get("/api/products/99")
        assert response.status_code == 404
    finally:
        app.dependency_overrides.pop(get_product_fetcher, None)

def fake_service_unavailable(product_id: int):
    request = httpx.Request(
        "GET", f"http://example.test/products/{product_id}"
    )
    raise httpx.ConnectError("Connection refused", request=request)

def provide_unavailable_product():
    return fake_service_unavailable

def test_service_unavailable(client):
    app.dependency_overrides[get_product_fetcher] = provide_unavailable_product
    try:
        response=client.get("/api/products/1")
        assert response.status_code == 503
    finally:
        app.dependency_overrides.pop(get_product_fetcher, None)