from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from database import engine


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

SessionDependency = Annotated[Session, Depends(get_session)]
