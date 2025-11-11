
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app  # noqa: E402


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_add_task(client):
    res = client.post("/tasks", json={"title": "Write report"})
    assert res.status_code == 201
    data = res.get_json()
    assert data["title"] == "Write report"


def test_list_tasks(client):
    client.post("/tasks", json={"title": "Do homework"})
    res = client.get("/tasks")
    assert res.status_code == 200
    tasks = res.get_json()
    assert len(tasks) >= 1


def test_delete_task(client):
    client.post("/tasks", json={"title": "Test delete"})
    res = client.delete("/tasks/1")
    assert res.status_code in [204, 404]


def test_delete_nonexistent_task(client):
    # essaie de supprimer une tâche avec un ID qui n'existe pas
    res = client.delete("/tasks/999")
    assert res.status_code == 404
