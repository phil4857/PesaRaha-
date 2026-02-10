# database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# -------------------------
# 1️⃣ Database URL
# -------------------------
# Read from environment variable
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL environment variable not set. "
        "Example: postgres://user:password@host:port/dbname"
    )

# -------------------------
# 2️⃣ SQLAlchemy engine
# -------------------------
engine = create_engine(DATABASE_URL)

# -------------------------
# 3️⃣ Session maker
# -------------------------
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# -------------------------
# 4️⃣ Base class for models
# -------------------------
Base = declarative_base()

# -------------------------
# 5️⃣ Dependency for FastAPI
# -------------------------
def get_db():
    """
    Yield a database session.
    Usage in FastAPI:
        def endpoint(db: Session = Depends(get_db))
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
