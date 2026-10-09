from fastapi import FastAPI

app = FastAPI(
    title="HeatDebt Backend",
    description="API service for HeatDebt.",
    version="0.1.0",
)


@app.get("/", tags=["health"])
def read_root() -> dict[str, str]:
    return {"service": "HeatDebt Backend", "status": "ok"}


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    return {"status": "healthy"}
