from sqlalchemy import Column, Integer, String
from db.connectiondb import Base, engine

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(Integer, unique=True, index=True)

Base.metadata.create_all(bind=engine)

print("✅ Tables created successfully!")