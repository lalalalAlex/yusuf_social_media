from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# lINK FOR DATABASE
SQLALCHEMY_DATABASE_URI = "sqlite:///pay.db"
# CONNECTING TO THE DATABASE
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# GENERATION FOR SESSIONS
SessionLocal = sessionmaker(bind=engine)


Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise

    finally:
        db.close()
