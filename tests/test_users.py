import pytest

def user_payload(
        name="Mike",
        email="mike@atu.ie",
        age=24,
        sid="S1234567",
):
    return {
        "name": name,
        "email": email,
        "age": age,
        "student_id": sid,
    }

# def test_create_user_returns_201(client):
#     response = client.post("/api/users", json=user_payload())

#     assert response.status_code == 201
#     data = response.json()
#     assert data["user_id"] == 1
#     assert data["name"] == "Mike"
#     assert data["email"] == "mike@atu.ie"

# def test_duplicate_user_id_returns_409(client):
#     client.post("/api/users", json=user_payload(uid=2))

#     response = client.post("/api/users", json=user_payload(uid =2))

#     assert response.status_code == 409
#     assert "exists" in response.json()["detail"].lower()

# @pytest.mark.parametrize(
#     "bad_student_id",
#     ["1234567", "s1234567", "S123", "S12345678"],
# )
# def test_bad_student_id_returns_422(client, bad_student_id):
#     response = client.post(
#         "/api/users",
#         json=user_payload(uid=3, sid=bad_student_id),
#     )
#     assert response.status_code == 422

# def test_get_users_returns_created_users(client):
#     client.post("/api/users", json=user_payload(uid=10, name="Alice", email="alice@atu.ie"))
#     response = client.get("/api/users")

#     assert response.status_code == 200
#     data = response.json()
#     assert len(data) == 1
#     assert data[0]["user_id"] == 10
#     assert data[0]["name"] == "Alice"

# def test_get_existing_user_returns_200(client):
#     client.post("/api/users", json=user_payload(uid=11))
#     response = client.get("/api/users/11")

#     assert response.status_code == 200
#     assert response.json()["user_id"] == 11

# def test_get_missing_user_returns_404(client):
#     response = client.get("/api/users/999")
#     assert response.status_code == 404
#     assert response.json()["detail"] == "User Not Found"

# def test_delete_existing_user_returns_204(client):
#     client.post("/api/users", json=user_payload(uid=20))
#     response = client.delete("/api/users/20")

#     assert response.status_code == 204
#     assert response.content == b''

# def test_delete_missing_user_returns_404(client):
#     response = client.delete("/api/users/999")

#     assert response.status_code == 404
#     assert response.json()["detail"] == "User Not Found"

# def test_deleted_user_can_no_longer_be_retrieved(client):
#     client.post("/api/users", json=user_payload(uid=21))
#     client.delete("/api/users/21")

#     response = client.get("/api/users/21")

#     assert response.status_code == 404

#NEW
def test_create_user_returns_201(client):
    response = client.post("/api/users", json=user_payload())
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Mike"

def test_duplicate_user_returns_409(client):
    client.post("/api/users", json=user_payload())

    response = client.post(
        "/api/users",
        json = user_payload(),
    )

    assert response.status_code == 409
    assert "already exists" in response.json()["detail"].lower()

def test_get_users(client):
    client.post("/api/users", json=user_payload())

    response=client.get("/api/users")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["student_id"] == "S1234567"

def test_get_user_by_id(client):
    created = client.post(
        "/api/users",
        json=user_payload(),
    ).json()

    user_id = created["id"]
    response = client.get(f"/api/users/{user_id}")

    assert response.status_code == 200
    assert response.json()["email"] == "mike@atu.ie"

def test_get_missing_user_returns_404(client):
    response = client.get("/api/users/999")

    assert response.status_code == 404
    assert "user not found" in response.json()["detail"].lower()

def test_delete_user(client):
    created=client.post(
        "/api/users",
        json=user_payload(),
    ).json()

    user_id = created["id"]

    response = client.delete(f"/api/users/{user_id}")
    assert response.status_code == 204

    response = client.get(f"/api/users/{user_id}")
    assert response.status_code == 404

def test_delete_missing_user_returns_404(client):
    response = client.delete("/api/users/999")

    assert response.status_code == 404

@pytest.mark.parametrize(
    "bad_sid",
    [
        "BAD123",
        "s1234567",
        "S123",
        "S122345678",
    ],
)
def test_invalid_student_id_returns_422(client, bad_sid):
    response = client.post(
        "/api/users",
        json=user_payload(sid=bad_sid),
    )

    assert response.status_code == 422