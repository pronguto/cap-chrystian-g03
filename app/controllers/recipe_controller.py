from dataclasses import asdict
from http import HTTPStatus

from app.configs.database import db
from app.models.exceptions.ingredient_exception import KeysError
from app.models.ingredient_model import Ingredient
from app.models.recipe_ingredients_model import RecipeIngredient
from app.models.production_recipes_model import ProductionRecipe
from app.models.recipe_model import Recipe
from app.models.exceptions.ingredient_exception import KeysError
from app.services import ingredient_service
from app.services.query_services import loader
from flask import jsonify, request
from flask_jwt_extended import jwt_required
from sqlalchemy import and_
from sqlalchemy.orm import Session


@jwt_required()
def create_recipe():
    data = request.get_json()
    expected_keys = {"recipe_name"}
    try:
        ingredient_service.validate_keys(body_request=data, expected_keys=expected_keys)
    except KeysError as e:
        return e.message, e.status_code
    recipe: Recipe = Recipe(**data)
    try:
        db.session.add(recipe)
        db.session.commit()
    except:
        return {"msg": "Recipe already exists"}, HTTPStatus.BAD_REQUEST
    return jsonify(recipe), HTTPStatus.CREATED


@jwt_required()
def recipe_ingredients_creator(id: int):
    data = request.get_json()
    expected_keys = {"ingredient_id", "quantity"}
    try:
        ingredient_service.validate_keys(body_request=data, expected_keys=expected_keys)
    except KeysError as e:
        return e.message, e.status_code
    recipe = Recipe.query.filter_by(recipe_id=id).first()
    payload = []
    recipe_ingredients: RecipeIngredient = RecipeIngredient(**data)
    setattr(recipe_ingredients, "recipe_id", id)
    db.session.add(recipe_ingredients)
    db.session.commit()
    prueba = RecipeIngredient.query.filter_by(recipe_id=id).all()
    payload.append(prueba)
    recipe_payload = asdict(recipe)
    recipe_payload.update({"receitas": payload})
    return recipe_payload, HTTPStatus.CREATED


@jwt_required()
def get_all_recipes():
    ingredients = db.session.query(Ingredient).all()
    ingredients = [asdict(ingredient) for ingredient in ingredients]
    recipes = db.session.query(Recipe).all()
    recipes = [asdict(recipe) for recipe in recipes]
    recipe_ingredients = db.session.query(RecipeIngredient).all()
    recipe_ingredients = [
        asdict(recipe_ingredient) for recipe_ingredient in recipe_ingredients
    ]
    output = []
    for recipe in recipes:
        recipe["ingredients"] = []
        for recipe_ingredient in recipe_ingredients:
            if recipe_ingredient["recipe_id"] == recipe["recipe_id"]:
                recipe["ingredients"].append(recipe_ingredient)
            for ingredient in ingredients:
                if ingredient["ingredient_id"] == recipe_ingredient["ingredient_id"]:
                    recipe_ingredient.update(
                        {"ingredient_name": ingredient["ingredient_name"]}
                    )
        output.append(recipe)
    return jsonify(output), HTTPStatus.OK

@jwt_required()
def get_recipe_by_name(name: str):
    ingredients = db.session.query(Ingredient).all()
    ingredients = [asdict(ingredient) for ingredient in ingredients]
    recipe = db.session.query(Recipe).filter_by(recipe_name=name.lower()).first()
    if not recipe:
        return {"Error": "Recipe not found"}, HTTPStatus.NOT_FOUND
    recipe = asdict(recipe)
    recipe_ingredients = db.session.query(RecipeIngredient).all()
    recipe_ingredients = [
        asdict(recipe_ingredient) for recipe_ingredient in recipe_ingredients
    ]
    output = []
    recipe["ingredients"] = []
    for recipe_ingredient in recipe_ingredients:
        if recipe_ingredient["recipe_id"] == recipe["recipe_id"]:
            recipe["ingredients"].append(recipe_ingredient)
            for ingredient in ingredients:
                if ingredient["ingredient_id"] == recipe_ingredient["ingredient_id"]:
                    recipe_ingredient.update(
                        {"ingredient_name": ingredient["ingredient_name"]}
                    )
    output.append(recipe)
    return jsonify(output), HTTPStatus.OK

@jwt_required()
def patch_recipe():
    data = request.get_json()
    session: Session = db.session()
    expected_keys = {"quantity", "recipe_id", "ingredient_id"}
    try:
        ingredient_service.validate_keys(body_request=data, expected_keys=expected_keys)
    except KeysError as e:
        return e.message, e.status_code
    patch_recipe_query = (
        session.query(RecipeIngredient)
        .filter(
            and_(
                RecipeIngredient.recipe_id == data["recipe_id"],
                RecipeIngredient.ingredient_id == data["ingredient_id"],
            )
        )
        .first()
    )
    if not patch_recipe_query:
        return {"error": "Recipe or ingredient not found"}, HTTPStatus.NOT_FOUND
    patch_recipe_query.quantity = data["quantity"]
    session.commit()
    return jsonify(patch_recipe_query), HTTPStatus.OK

@jwt_required()
def delete_recipe_by_id():
    data = request.args
    recipe_ingredients = (
        db.session.query(RecipeIngredient)
        .select_from(RecipeIngredient)
        .join(Recipe)
        .join(Ingredient)
        .filter(
            and_(
                Recipe.recipe_id == data["recipe_id"],
                Ingredient.ingredient_id == data["ingredient_id"],
            )
        )
        .first()
    )
    if not recipe_ingredients:
        return {"error": "id not found"}, 404
    db.session.delete(recipe_ingredients)
    db.session.commit()
    return "", HTTPStatus.NO_CONTENT


@jwt_required()
def delete_recipe(name: str):
    session: Session = db.session()
    recipe_del = Recipe.query.filter_by(recipe_name=name.lower()).first()
    if not recipe_del:
        return {"error": "Recipe not found"}, HTTPStatus.NOT_FOUND
    session.delete(recipe_del)
    session.commit()
    return "", HTTPStatus.NO_CONTENT

def delta():
    recetas = loader(Recipe)
    ingredientes = loader(Ingredient)
    robots = loader(RecipeIngredient)
    formulas = loader(ProductionRecipe)

    lista = []
    for receta in recetas:
        receta["ingredients"] = []
        petro = []
        for formula in formulas:
            if formula["recipe_id"] == receta["recipe_id"]:
                petro.append(formula["recipe_quantity"])
        for robot in robots:
            if robot["recipe_id"] == receta["recipe_id"]:
                receta["ingredients"].append(robot)
            for ingrediente in ingredientes:
                if ingrediente["ingredient_id"] == robot["ingredient_id"]:
                    robot.update({"ingredient_name": ingrediente["ingredient_name"]})
        receta["qty"] = sum(petro)
        lista.append(receta)
    
    return jsonify(lista)

