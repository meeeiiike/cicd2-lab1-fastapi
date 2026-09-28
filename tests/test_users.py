def user_payload(
        uid=1,
        name="Mike",
        email="mike@atu.ie",
        age=24,
        sid="S1234567",
):
    return {
        "user_id": uid,
        "name": name,
        "email": email,
        "age": age,
        "student_id": sid,
    }

def test_create_user_returns_201(client):
    response = client.post("/api/users", json=user_payload())

    assert response.status_code == 201
    data = response.json()
    assert data["user_id"] == 1
    assert data["name"] == "Mike"
    assert data["email"] == "mike@atu.ie"