from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Integer, String


@dataclass
class Recipe (db.Model):
    recipe_id: int
    recipe_name: str

    __tablename__ = "recipes"

    recipe_id = Column(Integer, primary_key = True)
    recipe_name = Column(String, nullable = False, unique = True)
    
    production = db.relationship("Production", secondary = "production_recipes", backref = "recipe")