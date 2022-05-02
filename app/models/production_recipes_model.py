from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship


@dataclass
class ProductionRecipe (db.Model):
    id:int
    production_id: int
    recipe_id: int
    recipe_quantity: float

    __tablename__ = "production_recipes"

    id = Column(Integer, primary_key = True)
    recipe_quantity = Column(Float(3), nullable = False)

    recipe_id = Column(Integer, ForeignKey("recipes.recipe_id"), nullable=False)
    production_id = Column(Integer, ForeignKey("productions.production_id"), nullable=False)

   