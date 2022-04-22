from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash


@dataclass
class User (db.Model):
    id: int
    user_name: str

    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    user_name = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)

    @property
    def password(self):
        raise AttributeError('Não é possivel acessar o atributo password')

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)
