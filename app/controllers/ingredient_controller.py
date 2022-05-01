from dataclasses import asdict
from http import HTTPStatus

from app.configs.database import db
from app.models.exceptions.ingredient_exception import KeysError
from app.models.ingredient_model import Ingredient
from app.models.ingredients_purchase_model import IngredientsPurchase
from app.services import ingredient_service
from flask import jsonify, request
from flask_jwt_extended import jwt_required
from sqlalchemy.orm import Query, Session


@jwt_required()
def ingredient_creator():
    data= request.get_json()
    session: Session= db.session()
    expected_keys= {"ingredient_name", "measurement_unit"}
    try:
        ingredient_service.validate_keys(body_request=data, expected_keys= expected_keys)
    except KeysError as e:
        return e.message, e.status_code
    for key, val in data.items():
        data[key]= val.lower()
        
    ingredient: Ingredient= Ingredient(**data)
    try:
        session.add(ingredient)
        session.commit()
    except:
        return {"msg": "ingredient already exists"}, HTTPStatus.BAD_REQUEST
    return jsonify(ingredient), HTTPStatus.CREATED

# @jwt_required()
def ingredient_loader():
    session: Session= db.session()

    base_query_ingredients: Query= session.query(Ingredient).all()
    sezalized_ingredients= []
    for ingredient in base_query_ingredients:
        base_query_ingredients_purchases: Query= session.query(
            IngredientsPurchase.purchase_id, 
            IngredientsPurchase.purchase_quantity, 
            IngredientsPurchase.purchase_price 
        ).filter_by(ingredient_id= ingredient.ingredient_id).all()
        purchase_ingredient_id=[]
        for purchase_ingredient in base_query_ingredients_purchases:
            purchase_ingredient_id.append(purchase_ingredient)
        to_seralize_ingredient=[]
        for purchase_id in purchase_ingredient_id:
            purchases_ingredient= {
            "purchase_id": purchase_id[0],
            "purchase_quantity": purchase_id[1],
            "purchase_price": purchase_id[2]
            }
            to_seralize_ingredient.append(purchases_ingredient)
        seralize_ingredient= {"purchases": to_seralize_ingredient}
        seralize_ingredient.update(asdict(ingredient))
        sezalized_ingredients.append(seralize_ingredient)

    return jsonify(sezalized_ingredients), HTTPStatus.OK

# @jwt_required()
def ingredient_by_name(name: str):
    session: Session= db.session()
    base_query_ingredient: Query= session.query(Ingredient).filter_by(ingredient_name= name.lower()).first()
    if not base_query_ingredient:
        return {"Error": "Ingredient not found"}, HTTPStatus.NOT_FOUND
    base_query_ingredient_purchase: Query= session.query(
        IngredientsPurchase.purchase_id, 
        IngredientsPurchase.purchase_quantity, 
        IngredientsPurchase.purchase_price 
    ).filter_by(ingredient_id= base_query_ingredient.ingredient_id).all()
    ingredient_purchase= []
    to_seralize_ingredient= []
    for purchase_ingredient in base_query_ingredient_purchase:
        ingredient_purchase.append(purchase_ingredient)
    for purchase_id in ingredient_purchase:
        purchases_ingredient= {
            "purchase_id": purchase_id[0],
            "purchase_quantity": purchase_id[1],
            "purchase_price": purchase_id[2] 
        }
        to_seralize_ingredient.append(purchases_ingredient)
    seralize_ingredient= {"purchases": to_seralize_ingredient}
    seralize_ingredient.update(asdict(base_query_ingredient))
    return jsonify(seralize_ingredient), HTTPStatus.OK

@jwt_required()
def ingredient_updater():
    data= request.get_json()
    session: Session= db.session()
    expected_keys= {"ingredient_name", "measurement_unit"}
    try:
        ingredient_service.validate_keys(body_request=data, expected_keys= expected_keys)
    except KeysError as e:
        return e.message, e.status_code
    for key, val in data.items():
        data[key]= val.lower()
    ingredient_patch= session.query(Ingredient).filter(Ingredient.ingredient_name==data["ingredient_name"].lower()).update({
        Ingredient.ingredient_name: data["ingredient_name"],
        Ingredient.measurement_unit: data["measurement_unit"]
    })
    if not ingredient_patch:
        return {"msg": "error, ingredient not found"}, HTTPStatus.BAD_REQUEST
    session.commit()
    ingredient: Ingredient= Ingredient.query.filter_by(ingredient_name= data["ingredient_name"]).first()
    return jsonify(ingredient), HTTPStatus.OK

@jwt_required()
def ingredient_deleter(name: str):
    session: Session= db.session()
    ingredient_delet= Ingredient.query.filter_by(ingredient_name= name.lower()).first()
    if not ingredient_delet:
        return {"Error": "Ingredient not found"}, HTTPStatus.NOT_FOUND
    session.delete(ingredient_delet)
    session.commit()
    return "", HTTPStatus.NO_CONTENT
