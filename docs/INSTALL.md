# Installing prerequisites

This file lists basic steps to set up a development environment for all supported OSes.

Note: PaddlePaddle / PaddleOCR installation is not required for Milestone 1, but will be required later. Detailed PaddlePaddle CPU instructions will be added in Milestone 2.

Common steps:
1. Install Python 3.11+ for your OS.
2. Create and activate a virtual environment.
3. Install pip requirements: pip install -r requirements.txt

For macOS:
- Install Python 3.11 via Homebrew: brew install python@3.11

For Windows:
- Use the official Python installer and make sure to add Python to PATH.

For Linux (Ubuntu/Debian):
- sudo apt update && sudo apt install python3.11 python3.11-venv python3.11-dev

HEIC support:
- iPhone photos may upload as HEIC. We will add HEIC handling in Milestone 2; for now please upload JPG/PNG. An open-source pillow plugin (pillow-heif) will be used later.
