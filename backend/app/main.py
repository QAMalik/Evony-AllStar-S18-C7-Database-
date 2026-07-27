import shutil
from pathlib import Path
from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List, Optional
import uuid
import os
from . import db as _db
from .models import Screenshot, Alliance
from datetime import datetime
from sqlmodel import Session, select

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TEMPLATES_DIR = BASE_DIR / "backend" / "app" / "templates"
STATIC_DIR = BASE_DIR / "backend" / "app" / "static"
UPLOAD_DIR = BASE_DIR / "backend" / "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI(title="Evony All-Star Analyzer")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

@app.on_event("startup")
def on_startup():
    _db.init_db()

@app.get("/", response_class=HTMLResponse)
def upload_page(request: Request):
    # For Milestone 1, return an empty alliances list if none exist
    alliances = []
    try:
        with _db.get_session() as session:
            stmt = select(Alliance.id, Alliance.name, Alliance.server)
            rows = session.exec(stmt).all()
            # convert to simple dicts for template
            alliances = [{"id": r[0], "name": r[1], "server": r[2]} for r in rows]
    except Exception:
        # safe fallback to empty list
        alliances = []
    return templates.TemplateResponse("upload.html", {"request": request, "alliances": alliances})

@app.post("/upload")
async def upload(request: Request, files: List[UploadFile] = File(...), screenshot_type: str = Form(...), alliance_id: Optional[int] = Form(None)):
    saved = []
    created_ids = []
    for up in files:
        contents = await up.read()
        suffix = Path(up.filename).suffix or ".jpg"
        fname = f"{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}_{uuid.uuid4().hex}{suffix}"
        dest = UPLOAD_DIR / fname
        with open(dest, "wb") as f:
            f.write(contents)
        # create DB record
        screenshot = Screenshot(
            filename=str(dest.relative_to(BASE_DIR)),
            uploader=None,
            processing_status="queued",
            uploaded_at=datetime.utcnow()
        )
        with _db.get_session() as session:
            session.add(screenshot)
            session.commit()
            session.refresh(screenshot)
            created_ids.append(screenshot.id)
        saved.append(str(dest))
    return JSONResponse({"uploaded": len(saved), "files": saved, "screenshot_ids": created_ids})

@app.get("/status")
def status():
    return {"status": "ok"}

@app.get("/alliances")
def list_alliances():
    # return list of alliances
    try:
        with _db.get_session() as session:
            stmt = select(Alliance)
            rows = session.exec(stmt).all()
            return [r.dict() for r in rows]
    except Exception:
        return []
