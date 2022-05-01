from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
)

from http import HTTPStatus
from flask import Flask, jsonify, request
from app.configs.database import db
from sqlalchemy.orm import Query, Session
from dataclasses import asdict
from app.models.recipe_model import Recipe
from flask_jwt_extended import jwt_required
from app.models.recipe_ingredients_model import RecipeIngredient
from app.models.ingredient_model import Ingredient

from app.services import ingredient_service
from app.models.exceptions.ingredient_exception import KeysError


#@jwt_required()
def create_recipe():
    data = request.get_json()

    recipe: Recipe = Recipe(**data)

    db.session.add(recipe)
    db.session.commit()

    return jsonify(recipe)

#@jwt_required()
def recipe_ingredients_creator(id):
    data = request.get_json()

    recipe = Recipe.query.filter_by(recipe_id = id).first()
    payload = []
    recipe_ingredients: RecipeIngredient = RecipeIngredient(**data)
    setattr(recipe_ingredients,"recipe_id",id)
    db.session.add(recipe_ingredients)
    db.session.commit()
    prueba = RecipeIngredient.query.filter_by(recipe_id = id).all()
    payload.append(prueba)
    recipe_payload = asdict(recipe)
    recipe_payload.update({
        "receitas": payload
    })
    return recipe_payload


#@jwt_required()
def get_all_recipes():
    session: Session = db.session()

    getrecipes: Query = (session.query(
        Recipe.recipe_name,
        Ingredient.ingredient_name,
        RecipeIngredient.quantity,
        )
        .select_from(Recipe)
        .join(Ingredient)
        .join(RecipeIngredient)
        .all()
    )
    
    all_recipes = [recipe._asdict() for recipe in getrecipes]

    return jsonify(all_recipes), HTTPStatus.OK

#@jwt_required()
def get_recipe_by_name(name: str):
    session: Session = db.session()

    recipe_by_name: Query= session.query(Recipe).filter_by(recipe_name = name.lower()).first()
    if not recipe_by_name:
        return {"error": "Recipe not found"}, HTTPStatus.NOT_FOUND
    
    return jsonify(recipe_by_name), HTTPStatus.OK


#@jwt_required()
def patch_recipe():
    data = request.get_json()
    session: Session= db.session()
    keys = {"recipe_name"}
    try:
       ingredient_service.validate_keys(body_request = data, keys = keys)

    except KeysError as e:
        return e.message, e.status_code

    for key, val in data.items():
        data[key]= val.lower()

    patch_recipe = session.query(Recipe).filter_by(Recipe.recipe_name == data["recipe_name"].lower()).update({
        Recipe.recipe_name: data["recipe_name"]})

    if not patch_recipe:
        return {"error": "Recipe not found"}, HTTPStatus.BAD_REQUEST

    session.commit()
    recipe: Recipe = Recipe.query.filter_by(recipe_name = data["recipe_name"]).first()
    return jsonify(recipe), HTTPStatus.OK



#@jwt_required()
def delete_recipe(name: str):
    session: Session = db.session()

    recipe_del = Recipe.query.filter_by(recipe_name = name.lower()).first()
    if not recipe_del:
        return {"error": "Recipe not found"}, HTTPStatus.NOT_FOUND

    session.delete(recipe_del)
    session.commit()
    return "", HTTPStatus.NO_CONTENT