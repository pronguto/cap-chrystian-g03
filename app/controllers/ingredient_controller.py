from app.configs.database import db
from app.models.ingredient_model import Ingredient
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm.session import Session
from http import HTTPStatus


# @jwt_required()
def ingredient_creator():
    data= request.get_json()
    session: Session= db.session()
    ingredient: Ingredient= Ingredient(**data)
    try:
        session.add(ingredient)
        session.commit()
    except:
        return {"msg": "error"}, HTTPStatus.BAD_REQUEST
    return jsonify(ingredient), HTTPStatus.CREATED

# @jwt_required()
def ingredient_loader():
    
    return {"msg": "ingredient loader"}

# def ingredient_by_name():
#     return {"msg": "ingredient by name"}

# @jwt_required()
def ingredient_updater():
    return {"msg": "ingredient updater"}

# @jwt_required()
def ingredient_deleter():
    return {"msg": "ingredient deleter"}
