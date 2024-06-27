import sys
import os
from unittest import TestCase
# from unittest.mock import MagicMock
# import mysql.connector


def removeLastPath(path: str):
    escape = "\\"

    path = path.split(escape)
    path.pop()
    path = escape.join(path)

    return path


correctPath = removeLastPath(os.path.abspath(__file__))
correctPath = removeLastPath(correctPath)
sys.path.append(correctPath)

from fastapi.testclient import TestClient
from src.main import app

# mock_session = MagicMock()

# def override_get_db():
#     try:
#         yield mock_session
#     finally:
#         pass


# app.dependency_overrides[get_database_connection] = override_get_db

client = TestClient(app)

class TestReservationController(TestCase):

    def test_health(self):
        response = client.get("/", headers={"X-Token": "coneofsilence"})
        assert response.status_code == 200
        assert response.json() == "Server is running"

