# Installation notes and commands for PaddleOCR and dependencies

See docs/INSTALL.md for detailed steps for Windows, macOS, and Linux. Milestone 1 does not require PaddleOCR to run; PaddleOCR will be installed and documented in Milestone 2. I included an INSTALL.md describing OS considerations and the plan for PaddlePaddle CPU installs.

Run the app (development):

1. Create a virtual environment

python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate     # Windows (PowerShell: .\.venv\Scripts\Activate.ps1)

2. Install dependencies

pip install -r requirements.txt

3. Start the FastAPI server

uvicorn backend.app.main:app --reload --port 8000

4. Open http://localhost:8000/ in your browser (or iPhone on same network)
