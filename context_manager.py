from fastapi import FastAPI
from sqlmodel import SQLModel
from database import engine
from contextlib import asynccontextmanager


# Initialize database tables
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Lifespan context manager for FastAPI to handle startup and shutdown.
    # Initializes the database and cleans up resources.

    try:
        async with engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)
        yield
    except Exception as e:
        raise
    finally:
        await engine.dispose()
