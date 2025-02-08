from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.db import Base, get_db
from main import app


SQLALCHEMY_DATABASE_URL = "sqlite:///test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False})
Base.metadata.create_all(engine)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False,
                                   bind=engine)


def override_get_db():
    session = TestingSessionLocal()
    yield session
    session.close()


app.dependency_overrides[get_db] = override_get_db


client = TestClient(app)


test_contestant = {
    "username": "test_user",
    "age": 25
}

PREFIX = "/api/v1"


def test_create_contestant():
    response = client.post(f"{PREFIX}/contestants", json=test_contestant)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == test_contestant["username"]
    assert data["age"] == test_contestant["age"]
    assert "id" in data


def test_get_contestant():
    create_response = client.post(f"{PREFIX}/contestants",
                                  json=test_contestant)
    contestant_id = create_response.json()["id"]

    response = client.get(f"{PREFIX}/contestants/{contestant_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == contestant_id
    assert data["username"] == test_contestant["username"]
    assert data["age"] == test_contestant["age"]


def test_get_non_existent_contestant():
    response = client.get("{PREFIX}/contestants/999")
    assert response.status_code == 404
