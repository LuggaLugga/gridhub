from sqlmodel import create_engine

from configuration import settings

engine = create_engine(str(settings.postgresql_url), echo=True)
