from sqlmodel import Field, SQLModel
from datetime import date


class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(unique=True)
    publisher: str
    publication_date: date
    page_count: int
    language: str


class BookReadModel(SQLModel):
    id: int
    title: str
    publisher: str
    publication_date: date
    page_count: int
    language: str


class BookCreateModel(SQLModel):
    title: str
    publisher: str
    publication_date: date
    page_count: int
    language: str


class BookUpdateModel(SQLModel):
    title: str | None = None
    publisher: str | None = None
    publication_date: date | None = None
    page_count: int | None = None
    language: str | None = None
