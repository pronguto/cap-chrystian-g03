from flask import jsonify
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
)

from app.models.purchase_model import Purchase
from app.models.ingredients_purchase_model import IngredientsPurchase
from app.models.ingredient_model import Ingredient
from sqlalchemy.orm import Query, Session
from app.configs.database import db

# @jwt_required()
def stock():
    session: Session = db.session
    query: Query = (
        session.query(Purchase.purchase_id,Purchase.purchase_date, Ingredient.ingredient_id,Ingredient.ingredient_name,IngredientsPurchase.purchase_quantity,IngredientsPurchase.purchase_price)
        .select_from(Purchase)
        .join(IngredientsPurchase)
        .join(Ingredient)
        # .filter(Purchase.purchase_id == purchase_id)
        .order_by(Purchase.purchase_id)
        .all()
    )
    purchases = [purchase._asdict() for purchase in query]
    # purchases = session.query(Purchase).all()
    return jsonify(purchases)