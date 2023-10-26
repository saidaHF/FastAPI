import sys
import os

from fastapi.testclient import TestClient
from src.__init__ import app, db

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(current_dir, '..')
sys.path.append(project_root)

client = TestClient(app)


def test_get_all_users():
    """
    Test get all users correctly
    """
    response = client.get("/api/v1/users")

    assert response.status_code == 200
    assert len(response.json()) == len(db)


def test_get_user_by_id():
    """
    Test valid id
    """
    user_id = str(db[1].id)
    response = client.get(f"/api/v1/users/{user_id}")

    assert response.status_code == 200
    assert response.json()["name"] == db[1].name


def test_get_user_by_invalid_id():
    """
    Test invalid id - not exists
    """
    user_id = "2dec8205-46f7-4317-8eb3-d586582d5ba8"
    response = client.get(f"/api/v1/users/{user_id}")

    assert response.status_code == 404


def test_create_user():
    """
    Test creating a new user
    """
    new_user = {"name": "Max Planck", "age": 89}
    response = client.post("/api/v1/users", json=new_user)

    assert response.status_code == 200
    created_user = db[-1]  # the last user is the new add user
    assert created_user.name == new_user["name"]
    assert created_user.age == new_user["age"]
    assert "id" in response.json()  # Verify that the new user to has a new id
    assert isinstance(response.json()["id"], str)  # id = UUID


def test_update_user():
    """
    Test for update a user exists
    """
    existing_user = db[0]
    updated_data = {"name": "Updated Name", "age": 35}
    response = client.put(f"/api/v1/users/{existing_user.id}", json=updated_data)

    assert response.status_code == 200
    # It searches for a user in the db list that has the same ID as the existing user's ID being sought
    # (in this case, existing_user). Once it finds that user, it assigns it to the updated_user variable so that you
    # can access its data and verify if the update was successful. If it doesn't find any user that meets the condition,
    # it could raise an exception if not handled properly.
    updated_user = next(user for user in db if user.id == existing_user.id)
    assert updated_user.name == updated_data["name"]
    assert updated_user.age == updated_data["age"]

    # verify in None case
    updated_data_with_null = {"name": None, "age": 40}
    response_with_null = client.put(f"/api/v1/users/{existing_user.id}", json=updated_data_with_null)
    assert response_with_null.status_code == 200

    updated_user_with_null = next(user for user in db if user.id == existing_user.id)
    assert updated_user_with_null.name == updated_user.name  # must save the last name
    assert updated_user_with_null.age == updated_data_with_null["age"]  # must update the age

