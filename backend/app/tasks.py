import time
from pathlib import Path
from .db import engine
from .models import Screenshot
from sqlmodel import Session, select
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent
UPLOAD_DIR = BASE_DIR / "backend" / "uploads"

def claim_next_screenshot(session: Session):
    # Simple selector; single worker expected.
    stmt = select(Screenshot).where(Screenshot.processing_status == 'queued').limit(1)
    res = session.exec(stmt).first()
    if not res:
        return None
    res.processing_status = 'processing'
    session.add(res)
    session.commit()
    session.refresh(res)
    return res

def process_screenshot(s: Screenshot):
    # Placeholder: do nothing yet
    print(f"Processing screenshot id={s.id}, filename={s.filename}")
    time.sleep(1)

if __name__ == '__main__':
    print("Starting worker loop. Press Ctrl+C to stop.")
    try:
        while True:
            with Session(engine) as session:
                s = claim_next_screenshot(session)
                if s:
                    try:
                        process_screenshot(s)
                        s.processing_status = 'done'
                    except Exception as e:
                        s.processing_status = 'error'
                        s.error_message = str(e)
                    session.add(s)
                    session.commit()
                else:
                    time.sleep(2)
    except KeyboardInterrupt:
        print("Worker stopped")
