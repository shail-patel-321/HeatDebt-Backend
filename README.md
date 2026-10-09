# HeatDebt Backend

A FastAPI backend service for HeatDebt.

## Setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run

```powershell
uvicorn app.main:app --reload
```

The API is available at `http://127.0.0.1:8000`. Interactive documentation is at `/docs`.

## Test

```powershell
pytest
```
