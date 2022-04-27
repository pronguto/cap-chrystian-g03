from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, Integer, String, DateTime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import func


@dataclass
class User (db.Model):

    id: int
    name: str
    email: str

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False )
    password_hash = Column(String, nullable=False)


    @property
    def password(self):
        raise AttributeError("Inaccessible password")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)
