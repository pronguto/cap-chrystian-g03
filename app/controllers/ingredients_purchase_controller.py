from dataclasses import asdict
from flask import jsonify, request
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
)

from app.models.ingredients_purchase_model import IngredientsPurchase
from app.models.purchase_model import Purchase
from app.models.ingredient_model import Ingredient
from app.configs.database import db
from app.controllers.ingredient_controller import ingredient_creator

def ingredients_purchase_creator(id):
    data = request.get_json()
    payload = []
    
    x = data.pop("ingredient_name")
    ingredient = Ingredient.query.filter_by(ingredient_name = x).first()
    # if Ingredient.query.filter_by(ingredient_name = x).first():
    #     ingredient = Ingredient.query.filter_by(ingredient_name = x).first()
    # else:
    #     ingrediente = Ingredient(**{"ingredient_name": x})
    #     db.session.add(ingrediente)
    #     db.session.commit()
    #     ingredient = ingrediente
    
    ingredient_id = asdict(ingredient)["ingredient_id"]
    purchase = Purchase.query.filter_by(purchase_id = id).first()
    ingredients_purchase: IngredientsPurchase = IngredientsPurchase(**data)
    
    setattr(ingredients_purchase,"purchase_id",id)
    setattr(ingredients_purchase,"ingredient_id",ingredient_id)
    
    db.session.add(ingredients_purchase)
    db.session.commit()
    
    prueba = IngredientsPurchase.query.filter_by(purchase_id = id).all()
    payload.append(prueba)
    purchase_payload = asdict(purchase)
    purchase_payload.update({
        "compras": payload
    })
    return  purchase_payload

# @jwt_required()
def ingredients_purchase_loader():
    ingredients_purchase = IngredientsPurchase.query.all()
    return jsonify(ingredients_purchase)

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