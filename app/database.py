import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# رابط قاعدة البيانات (SQLite للتجربة، يمكن تغييره لـ PostgreSQL على السيرفر)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./digital_products.db")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
