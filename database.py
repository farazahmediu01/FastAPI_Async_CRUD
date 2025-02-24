from typing import Annotated, AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session
from fastapi import Depends

# aiosqlite provides a friendly, async interface to sqlite databases.
DATABASE_URL = "sqlite+aiosqlite:///database.db"

# Async database setup.
engine = create_async_engine(
    DATABASE_URL, echo=True, future=True, connect_args={"check_same_thread": False}
)

# Async Sesion.
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


# Dependency Injection.
session_dependency = Annotated[AsyncSession, Depends(get_session)]
