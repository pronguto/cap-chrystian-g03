from app.models.purchase_model import Purchase
from app.models.ingredients_purchase_model import IngredientsPurchase
from app.models.ingredient_model import Ingredient
from app.configs.database import db
from dataclasses import asdict

def loader(model):
    lista = db.session.query(model).all()
    lista = [asdict(item) for item in lista]
    return lista
