import os
from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app import db
from sqlmodel import SQLModel, create_engine
import tempfile
from pathlib import Path

client = TestClient(app)

def test_db_migration():
    # Create a temporary DB and ensure metadata.create_all runs
    tmp = tempfile.NamedTemporaryFile(suffix='.db', delete=False)
    tmp.close()
    url = f"sqlite:///{tmp.name}"
    engine = create_engine(url, connect_args={"check_same_thread": False})
    SQLModel.metadata.create_all(engine)
    # check file exists
    assert Path(tmp.name).exists()
    os.unlink(tmp.name)

def test_upload_endpoint(tmp_path):
    # Use TestClient to POST a small file
    file_path = tmp_path / "test.jpg"
    file_path.write_bytes(b"\xff\xd8\xff\xd9")  # minimal JPEG bytes
    with open(file_path, 'rb') as f:
        response = client.post('/upload', files={'files': ('test.jpg', f, 'image/jpeg')}, data={'screenshot_type': 'type1'})
    assert response.status_code == 200
    data = response.json()
    assert 'uploaded' in data and data['uploaded'] >= 1
