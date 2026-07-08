from fastapi.testclient import TestClient
from api.main import app
import datetime
from pathlib import Path

client = TestClient(app)

# Test data 
document_md = "data/sample/short_story_testing.md"


def test_api_check():
  
  response = client.get("/health-check")

  assert response.status_code == 200
  body = response.json()
  assert body["status"] == "healthy"
  datetime.datetime.fromisoformat(body["timestamp"])


def test_chunking_document_happy():
  short_md = Path("data/sample/short_story_testing.md")

  with short_md.open("rb") as f:
    response = client.post(
            "/chunking-document",
            files={"file": (short_md.name, f, "text/markdown")},
        )

  assert response.status_code == 200
  body = response.json()
  assert "metadata" in body
  assert "chunks" in body

def test_chunking_document_failure():
  empty_text = Path("data/sample/empty.txt")

  with empty_text.open("rb") as f:
    response = client.post(
            "/chunking-document",
            files={"file": (empty_text.name, f, "text/text")},
        )
    
  assert response.status_code == 500
  body = response.json()
  assert body["detail"] == "The file is empty"
  
 



