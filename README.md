# CICD-2 FastAPI Lab Template

This repository contains a FastAPI lab for the CICD-2 module.  
Use this `README.md` as the standard structure for future labs.

---

## Lab Title

**Lab 5 — Two FastAPI Microservices with HTTPX**
---
## Repository Structure

```text
app/ # Existing User API
├── __init__.py
├── main.py # Keep existing user routes
├── database.py # Keep get_db / SessionLocal
├── models.py # Keep UserDB
├── schemas.py # Keep UserCreate / UserRead
└── product_client.py # NEW: external HTTP client

product_service/ # NEW: second FastAPI application
├── __init__.py
└── main.py

tests/
├── conftest.py # Keep Lab 4 database fixtures
├── test_users.py # Keep Lab 4 tests
└── test_remote_products.py # NEW: endpoint tests
```

---

## Running the Services in Codespaces

Open two terminals in the same Codespace.

**User Service (port 8000) - Terminal 1**
```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

**Product Service (port 8001) - Terminal 2**
```bash
python -m uvicorn product_service.main:app --host 0.0.0.0 --port 8001 --reload
```
** In the Codespaces Ports tab, open port 8000 to access the User API or port 8001 to access the Product Service. Append /docs to either forwarded URL to view that service’s API documentation. **

## Get a Product

The User API provides this endpoint:
```text
 GET /api/products/{product_id} 
```

For example, request GET /api/products/1 from the User API’s port-8000 URL. A successful response looks like:
```text
{"id": 1, "name": "Laptop", "price": 899.0}
```

The endpoint forwards the request to the Product Service. An unknown product returns 404; if the Product Service is unavailable, the User API returns 503.


## Product Service URL

PRODUCT_SERVICE_URL is the base URL the User API uses to reach the Product Service. The User API appends /products/{product_id} to it. In Codespaces, its default is http://127.0.0.1:8001, which works when both services run in the same Codespace. Set this variable on the User API process only if the Product Service is at a different address. For example, in a Docker Compose setup, it could be http://product-service:8001. 
