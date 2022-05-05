import json
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
from app.models.ingredient_model import Ingredient
from flask_jwt_extended import jwt_required
from app.models.recipe_ingredients_model import RecipeIngredient
from sqlalchemy import and_
from app.models.exceptions.ingredient_exception import KeysError
from app.services import ingredient_service
from app.services.query_services import loader


# @jwt_required()
def create_recipe():
    data = request.get_json()
    recipe: Recipe = Recipe(**data)

    db.session.add(recipe)
    db.session.commit()

    return jsonify(recipe)


# @jwt_required()
def recipe_ingredients_creator(id):
    data = request.get_json()
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
    return recipe_payload


# @jwt_required()
def get_all_recipes():
    ingredients = db.session.query(Ingredient).all()
    ingredients = [asdict(ingredient) for ingredient in ingredients]
    recipes = db.session.query(Recipe).all()
    recipes = [asdict(recipe) for recipe in recipes]
    recipe_ingredients = db.session.query(RecipeIngredient).all()
    recipe_ingredients = [
        asdict(recipe_ingredient) for recipe_ingredient in recipe_ingredients
    ]

    teste = []
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

        teste.append(recipe)
    return jsonify(teste)


# @jwt_required()
def patch_recipe(id):
    new_data = request.get_json()

    recipe_ingredients = (
        db.session.query(RecipeIngredient).filter_by(recipe_id=id).first()
    )

    for key, value in new_data.items():
        setattr(recipe_ingredients, key, value)
        print(f"****{recipe_ingredients}")

    db.session.add(recipe_ingredients)
    db.session.commit()

    return jsonify(recipe_ingredients), HTTPStatus.OK


# @jwt_required()
def get_recipe_by_name(name):
    ingredients = db.session.query(Ingredient).all()
    ingredients = [asdict(ingredient) for ingredient in ingredients]
    recipe = db.session.query(Recipe).filter_by(recipe_name=name.lower()).first()
    recipe = asdict(recipe)
    recipe_ingredients = db.session.query(RecipeIngredient).all()
    recipe_ingredients = [
        asdict(recipe_ingredient) for recipe_ingredient in recipe_ingredients
    ]

    teste = []
    recipe["ingredients"] = []
    for recipe_ingredient in recipe_ingredients:
        if recipe_ingredient["recipe_id"] == recipe["recipe_id"]:
            recipe["ingredients"].append(recipe_ingredient)
            for ingredient in ingredients:
                if ingredient["ingredient_id"] == recipe_ingredient["ingredient_id"]:
                    recipe_ingredient.update(
                        {"ingredient_name": ingredient["ingredient_name"]}
                    )

            teste.append(recipe)
        return jsonify(teste)


# @jwt_required()
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
    return "", 204


# @jwt_required()
def delete_recipe(name):
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

    items_list = []
    for ingrediente in ingredientes:
        ingrediente["recipes"] = []
        for robot in robots:
            if robot["ingredient_id"] == ingrediente["ingredient_id"]:
                ingrediente["recipes"].append(robot)
        items_list.append(ingrediente)

    return jsonify(items_list)

