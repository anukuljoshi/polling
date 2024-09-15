from fastapi import status
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_item():
    """test read item handler"""
    response = client.get("/items/foo", headers={"X-Token": "coneofsilence"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "id": "foo",
        "title": "Foo",
        "description": "There goes my hero",
    }


def test_read_item_bad_token():
    """test read item handler with bad token"""
    response = client.get("/items/foo", headers={"X-Token": "hailhydra"})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": "Invalid X-Token header"}


def test_read_nonexistent_item():
    """test read item handler with non existent item"""
    response = client.get("/items/baz", headers={"X-Token": "coneofsilence"})
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Item not found"}


def test_create_item():
    """test create item"""
    response = client.post(
        "/items/",
        headers={"X-Token": "coneofsilence"},
        json={
            "id": "foobar",
            "title": "Foo Bar",
            "description": "The Foo Barters",
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "id": "foobar",
        "title": "Foo Bar",
        "description": "The Foo Barters",
    }


def test_create_item_bad_token():
    """test create item with bad token"""
    response = client.post(
        "/items/",
        headers={"X-Token": "hailhydra"},
        json={"id": "bazz", "title": "Bazz", "description": "Drop the bazz"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": "Invalid X-Token header"}


def test_create_existing_item():
    """test create item with existing item"""
    response = client.post(
        "/items/",
        headers={"X-Token": "coneofsilence"},
        json={
            "id": "foo",
            "title": "The Foo ID Stealers",
            "description": "There goes my stealer",
        },
    )
    assert response.status_code == status.HTTP_409_CONFLICT
    assert response.json() == {"detail": "Item already exists"}
