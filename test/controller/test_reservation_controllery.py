import sys
import os


def removeLastPath(caminho: str):
    escape = "\\"

    caminho = caminho.split(escape)
    caminho.pop()
    caminho = escape.join(caminho)

    return caminho


correctPath = removeLastPath(os.path.abspath(__file__))
correctPath = removeLastPath(correctPath)
sys.path.append(correctPath)


from parking.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_health():
    response = client.get("/", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json() == {"Server is running"}
