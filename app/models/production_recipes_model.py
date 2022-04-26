from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Float, ForeignKey, Integer


@dataclass
class ProductionRecipe (db.Model):
    production_id: int
    recipe_id: int
    recipe_quantity: float

    __tablename__ = "production_recipes"

    id = Column(Integer, primary_key = True)
    production_id = Column(Integer, ForeignKey("productions.production_id"), nullable=False)
    recipe_id = Column(Integer, ForeignKey("recipes.recipe_id"), nullable=False)
    recipe_quantity = Column(Float(3), nullable = False)
    
