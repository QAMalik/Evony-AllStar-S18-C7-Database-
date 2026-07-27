# Evony All-Star Analyzer

## Project Vision
Build a local, open-source tool that allows alliance leaders and analysts to import Evony All-Star screenshots, extract alliance and player data using local OCR (PaddleOCR), validate entries with Evony-specific rules, and export results to Excel for qualification analysis. The tool must run entirely offline, support batch imports, and be mobile-friendly (iPhone Safari compatible).

## Current Architecture
- Backend: Python 3.11 + FastAPI — chosen for asynchronous request handling, easy templating with Jinja2, and excellent developer ergonomics.
- Templating/UI: Jinja2 + Bootstrap 5 — lightweight, mobile-friendly UI without client-side SPA frameworks, ensuring Safari compatibility.
- Database: SQLite — simple, file-based, cross-platform storage suitable for local deployments and easy backups.
- OCR: PaddleOCR (local) — open-source OCR engine required to run entirely locally without paid services.
- Image processing: OpenCV + Pillow — robust image manipulation and preprocessing for OCR.
- Excel export: openpyxl — pure-Python Excel writer, no external services.

Why these choices:
- All components are free and open-source and can run locally on Windows, macOS, and Linux.
- FastAPI + Jinja2 delivers a server-rendered UI that works on iPhone Safari without heavy JS dependencies.
- SQLite simplifies installation while remaining extensible for future migration to Postgres if needed.

## Milestones

- Milestone 0: Pre-setup (Complete)
  - Objectives: Create docs and initial planning.
  - Deliverables: docs/INSTALL.md, ARCHITECTURE notes.
  - Date completed: (append when completed)
  - Notes: Initial planning completed.

- Milestone 1: Repository skeleton, DB schema, FastAPI, Bootstrap upload UI (In Progress / Complete after approval)
  - Status: In Progress
  - Objectives:
    - Create folder structure and migration SQL
    - Implement FastAPI app with Jinja2 templates
    - Create upload endpoint accepting batch uploads and persisting screenshots with processing_status='queued'
    - Provide a separate worker process skeleton
  - Deliverables:
    - repository structure, database/migrations/000_init.sql
    - backend/app with main.py, db.py, models.py, tasks.py
    - templates/upload.html and static assets
    - tests/test_basic.py
    - docs/RUNNING.md and docs/INSTALL.md
  - Date completed: (to be filled when you accept Milestone 1)
  - Notes: Waiting for user acceptance before proceeding.

- Milestone 2: OCR pipeline & validation (Not Started)
  - Objectives:
    - Integrate PaddleOCR locally
    - Implement OpenCV/Pillow preprocessing
    - Implement rule-based row/column segmentation and parsing for Type 1 and Type 2
    - Implement lenient validation engine and import_log persistence
  - Deliverables:
    - ocr/ modules, parsing and validation saving to DB
    - screenshot processing worker implementation
  - Date completed: 
  - Notes: 

- Milestone 3: Manual review UI & reprocessing (Not Started)
  - Objectives: UI for correcting parsed rows and re-running OCR on images
  - Deliverables: Templates and endpoints for manual edits

- Milestone 4: Excel Export & dynamic stats (Not Started)
  - Objectives: Implement openpyxl export with three sheets (Alliance Summary, Players, Import Log)
  - Deliverables: /export endpoint and worker job

- Milestone 5: HEIC support, HEIF decoding, cross-platform installs (Not Started)
  - Objectives: Add pillow-heif or pyheif support and test on macOS/iPhone HEIC images

- Milestone 6: Improved segmentation/ML models (Not Started)
  - Objectives: If needed, add training dataset and small detection model to improve layout detection

## Future Features
- Support multiple All-Star seasons and historical comparisons
- Alliance classifications (Purpose-built, Likely Purpose-built, Standard)
- Better OCR models and tuning (still using PaddleOCR but improved preprocessing and possible model fine-tuning)
- Faster batch imports (parallel workers, but respect SQLite concurrency limitations)
- Advanced statistics (time-series analyses, comparisons across seasons)
- Excel improvements (pivot tables, preformatted charts)

## Design Decisions
- Local-only architecture: all OCR and processing are local to satisfy privacy and cost constraints.
- SQLite first: simple file DB for local users, easy to migrate later; worker is single-process-friendly.
- DB-backed queue: to avoid external dependencies like Redis/Celery—worker process polls DB and claims queued rows.
- Server-rendered UI: Jinja2+Bootstrap ensures full functionality on iPhone Safari without heavy JS frameworks.

## Known Limitations
- Current implementation (Milestone 1) uses placeholder static assets and does not yet include OCR decoding.
- HEIC decoding not implemented yet (planned Milestone 2).
- Rule-based segmentation may not handle all UI variants — may require ML in later milestones.
- SQLite single-writer limits concurrent heavy writes; design uses single worker to mitigate.

## Changelog
- (Initial) Created project skeleton and Milestone 1 artifacts. Pending user acceptance to mark Milestone 1 complete.


