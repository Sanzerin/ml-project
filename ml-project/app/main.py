"""Простое FastAPI-приложение с эндпоинтом проверки работоспособности."""
from fastapi import FastAPI

app = FastAPI(title="ML Project", version="0.1.0")


@app.get("/ping")
def ping() -> dict[str, str]:
    """Health-check: GET /ping -> {"status": "ok"}."""
    return {"status": "ok"}
