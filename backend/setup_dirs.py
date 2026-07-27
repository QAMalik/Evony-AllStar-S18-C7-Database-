from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "backend" / "uploads"
EXPORTS_DIR = BASE_DIR / "exports" / "generated"

for d in [UPLOAD_DIR, EXPORTS_DIR]:
    os.makedirs(d, exist_ok=True)

DATABASE_FILE = BASE_DIR / "database" / "app.db"
