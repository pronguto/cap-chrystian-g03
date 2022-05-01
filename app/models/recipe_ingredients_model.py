from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Float, ForeignKey, Integer, Numeric, String


@dataclass
class RecipeIngredient (db.Model):
    ingredient_id: int
    quantity: float
    recipe_id: int

    __tablename__ = "recipe_ingredients"

    id = Column(Integer, primary_key = True)
    recipe_id = Column(Integer, ForeignKey("recipes.recipe_id"), nullable=False)
    ingredient_id = Column(Integer, ForeignKey("ingredients.ingredient_id"), nullable=False)
    quantity = Column(Float(3), nullable = False)

