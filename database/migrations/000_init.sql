# SQLite migration: create required tables for Milestone 1

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS seasons (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE,
  start_date DATE,
  end_date DATE,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME
);

CREATE TABLE IF NOT EXISTS boc_rounds (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  season_id INTEGER NOT NULL,
  name TEXT NOT NULL,
  start_date DATE,
  end_date DATE,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  UNIQUE (season_id, name),
  FOREIGN KEY (season_id) REFERENCES seasons(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS alliances (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  season_id INTEGER NOT NULL,
  boc_round_id INTEGER,
  server TEXT,
  name TEXT NOT NULL,
  alliance_rank INTEGER,
  current_score INTEGER,
  win_percentage REAL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  UNIQUE (season_id, name, server),
  FOREIGN KEY (season_id) REFERENCES seasons(id) ON DELETE CASCADE,
  FOREIGN KEY (boc_round_id) REFERENCES boc_rounds(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS players (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  alliance_id INTEGER NOT NULL,
  name TEXT NOT NULL,
  keep_level INTEGER,
  power INTEGER,
  monarch_level INTEGER,
  first_seen DATETIME,
  last_seen DATETIME,
  source_screenshot_id INTEGER,
  validated INTEGER DEFAULT 0,
  validation_notes TEXT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (alliance_id) REFERENCES alliances(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS screenshots (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  season_id INTEGER,
  boc_round_id INTEGER,
  alliance_id INTEGER,
  filename TEXT NOT NULL,
  uploader TEXT,
  image_width INTEGER,
  image_height INTEGER,
  uploaded_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  processing_status TEXT DEFAULT 'queued',
  error_message TEXT,
  raw_ocr_text TEXT,
  parsed_json TEXT,
  FOREIGN KEY (season_id) REFERENCES seasons(id),
  FOREIGN KEY (boc_round_id) REFERENCES boc_rounds(id),
  FOREIGN KEY (alliance_id) REFERENCES alliances(id)
);

CREATE TABLE IF NOT EXISTS import_log (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  screenshot_id INTEGER,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  level TEXT NOT NULL,
  code TEXT,
  message TEXT NOT NULL,
  details TEXT,
  FOREIGN KEY (screenshot_id) REFERENCES screenshots(id) ON DELETE CASCADE
);
