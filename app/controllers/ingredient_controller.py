from http import HTTPStatus

from app.configs.database import db
from app.models.exceptions.ingredient_exception import KeysError
from app.models.ingredient_model import Ingredient
from flask import jsonify, request
from flask_jwt_extended import jwt_required
from sqlalchemy.orm import Query, Session
from app.services import ingredient_service


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

@jwt_required()
def ingredient_loader():
    session: Session= db.session()

    base_query: Query= session.query(Ingredient).all()

    ingredients= base_query

    return jsonify(ingredients), HTTPStatus.OK

# def ingredient_by_name():
#     return {"msg": "ingredient by name"}

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