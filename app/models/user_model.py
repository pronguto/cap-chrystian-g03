from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Integer, String


@dataclass
class User (db.Model):
    id: int
    user_name: str

    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    user_name = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
