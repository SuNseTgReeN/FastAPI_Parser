from fastapi import FastAPI

from src.parser.routers import router

app = FastAPI(
    title="FastAPI Parser",
)

app.include_router(router)
