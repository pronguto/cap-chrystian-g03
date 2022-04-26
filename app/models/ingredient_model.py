from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Integer, String

@dataclass
class Ingredient (db.Model):
    ingredient_id: int
    ingredient_name: str
    measurement_unit: str

    __tablename__ = "ingredients"

    ingredient_id = Column(Integer, primary_key = True)
    ingredient_name = Column(String, nullable = False, unique = True)
    measurement_unit = Column(String(10), nullable = False)
    
    recipe = db.relationship("Recipe", secondary = "recipe_ingredients", backref = "ingredient")
