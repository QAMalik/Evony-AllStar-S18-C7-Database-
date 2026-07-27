# Commands and notes

Run server:

uvicorn backend.app.main:app --reload --port 8000

Run worker (separate process):

python -m backend.app.tasks

Run tests:

pytest -q

Database file will be created at ./database/app.db
Uploaded files saved to backend/uploads/
Generated exports go to exports/generated/
