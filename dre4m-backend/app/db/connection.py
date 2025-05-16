# From imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from settings.settings import get_settings


settings = get_settings()


DATABASE_URL = settings.DATABASE_URL

# Creates database engine with lazy initialization
# SSOT: Engine only created once
# https://en.wikipedia.org/wiki/Single_source_of_truth
# https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine
engine = create_engine(DATABASE_URL)

# Created session uses the same instance of the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative class definitions
# Base.metadata.create_all(bind=engine)
Base = declarative_base()
