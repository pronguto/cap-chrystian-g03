from datetime import datetime
from flask import jsonify, request
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from psycopg2 import Date

from app.models.purchase_model import Purchase
from app.models.ingredients_purchase_model import IngredientsPurchase
from app.models.ingredient_model import Ingredient
from sqlalchemy.orm import Query, Session
from app.configs.database import db
from sqlalchemy import  and_

def purchase_creator():
    purchase: Purchase = Purchase()
    db.session.add(purchase)
    db.session.commit()
    return  jsonify(purchase)

# @jwt_required()
def purchase_loader():
    purchases = Purchase.query.all()
    return jsonify(purchases)

@jwt_required()
def purchase_intervaler():
    return {"msg": "purchase intervaler"}

# def purchase_by_date():
#     return {"msg": "purchase by date"}

@jwt_required()
def purchase_updater():
    return {"msg": "purchase updater"}

@jwt_required()
def purchase_deleter():
    return {"msg": "purchase deleter"}

def purchase_intervaler():
    session: Session = db.session
    data = request.args
    initial_date = datetime.strptime(data["initial_date"],"%d/%m/%Y").date()
    final_date = datetime.strptime(data["final_date"], "%d/%m/%Y").date()
    query: Query = (
        session.query(Purchase.purchase_id,Purchase.purchase_date, Ingredient.ingredient_id,Ingredient.ingredient_name,IngredientsPurchase.purchase_quantity,IngredientsPurchase.purchase_price)
        .select_from(Purchase)
        .join(IngredientsPurchase)
        .join(Ingredient)
        # from sqlalchemy import and_
        .filter(and_(Purchase.purchase_date > initial_date, Purchase.purchase_date < final_date))
        .order_by(Purchase.purchase_id)
        .all()
    )
    purchases = [purchase._asdict() for purchase in query]
    return jsonify(purchases)

def sumator():
    x = 42
    y = 35
    return {"suma": x + y}