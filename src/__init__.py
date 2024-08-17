from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager


@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"Server has started")
    yield
    print(f"Server has stopped")


version = "v1"

app = FastAPI(
    title="Bookify",
    version=version,
    description="A Rest api endpoint for getting all the books",
    lifespan=life_span
)

app.include_router(
    book_router, prefix=f"/api/{version}/books", tags=["books"])
