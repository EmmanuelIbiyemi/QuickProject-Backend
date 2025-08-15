from sqlalchemy import Column, Integer, String
from .connectiondb import Base

class User(Base):
    tabname:str = "User"

    name = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(Integer, unique=True, index=True)