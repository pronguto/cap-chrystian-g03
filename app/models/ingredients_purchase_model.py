from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Float, ForeignKey, Integer, Numeric

from sqlalchemy.orm import relationship


@dataclass
class IngredientsPurchase (db.Model):
    purchase_id: int
    ingredient_id: int
    purchase_quantity: float
    purchase_price: float

    __tablename__ = "ingredients_purchase"

    id = Column(Integer, primary_key = True)
    purchase_quantity = Column(Float(3), nullable = False)
    purchase_price = Column(Numeric(asdecimal = False))

    ingredient_id = Column(
            Integer, ForeignKey("ingredients.ingredient_id"), nullable=False
        )

    purchase_id = Column(Integer, ForeignKey("purchases.purchase_id"), nullable=False)
    
  

