from dataclasses import dataclass
from datetime import datetime

from app.configs.database import db
from sqlalchemy import Column, Date, Integer

from app.models.ingredients_purchase_model import IngredientsPurchase


@dataclass
class Purchase (db.Model):
    purchase_id: int
    purchase_date: str

    __tablename__ = "purchases"

    purchase_id = Column(Integer, primary_key = True)
    purchase_date = Column(Date, default = datetime.now())

    ingredients = db.relationship("Ingredient", secondary = IngredientsPurchase, backref = "purchase")
    
