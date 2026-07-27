from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Season(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    created_at: Optional[datetime] = None

class BOCRound(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    season_id: int
    name: str
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    created_at: Optional[datetime] = None

class Alliance(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    season_id: int
    boc_round_id: Optional[int] = None
    server: Optional[str] = None
    name: str
    alliance_rank: Optional[int] = None
    current_score: Optional[int] = None
    win_percentage: Optional[float] = None
    created_at: Optional[datetime] = None

class Player(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    alliance_id: int
    name: str
    keep_level: Optional[int] = None
    power: Optional[int] = None
    monarch_level: Optional[int] = None
    first_seen: Optional[datetime] = None
    last_seen: Optional[datetime] = None
    source_screenshot_id: Optional[int] = None
    validated: Optional[int] = 0
    validation_notes: Optional[str] = None
    created_at: Optional[datetime] = None

class Screenshot(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    season_id: Optional[int] = None
    boc_round_id: Optional[int] = None
    alliance_id: Optional[int] = None
    filename: str
    uploader: Optional[str] = None
    image_width: Optional[int] = None
    image_height: Optional[int] = None
    uploaded_at: Optional[datetime] = None
    processing_status: Optional[str] = "queued"
    error_message: Optional[str] = None
    raw_ocr_text: Optional[str] = None
    parsed_json: Optional[str] = None

class ImportLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    screenshot_id: Optional[int] = None
    created_at: Optional[datetime] = None
    level: str
    code: Optional[str] = None
    message: str
    details: Optional[str] = None
