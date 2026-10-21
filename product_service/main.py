from fastapi import FastAPI, HTTPException

app = FastAPI(title="Product Service")

PRODUCTS={
    1: {"id": 1, "name": "Laptop", "price": 899.00},
    2: {"id": 2, "name": "Mouse", "price": 25.0},
}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    product = PRODUCTS.get(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product Not Found")
    return product

@app.get("/products")
def get_products():
    products = list(PRODUCTS.values())
    return products

