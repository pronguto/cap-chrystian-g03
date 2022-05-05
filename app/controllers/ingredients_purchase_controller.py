from dataclasses import asdict
from http import HTTPStatus
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
from app.services import ingredient_service
from app.models.exceptions.ingredient_exception import KeysError

jwt_required()
def ingredients_purchase_creator(id):
    data = request.get_json()
    payload = []
    expected_keys = {"ingredient_name", "purchase_quantity", "purchase_price"}
    try:
        ingredient_service.validate_keys(body_request=data, expected_keys= expected_keys)
    except KeysError as e:
        return e.message, e.status_code

    x = data.pop("ingredient_name")
    if Ingredient.query.filter_by(ingredient_name=x).first():
        ingredient = Ingredient.query.filter_by(ingredient_name=x).first()
    else:
        ingrediente = Ingredient(**{"ingredient_name": x})
        db.session.add(ingrediente)
        db.session.commit()
        ingredient = ingrediente
    ingredient_id = asdict(ingredient)["ingredient_id"]
    purchase = Purchase.query.filter_by(purchase_id=id).first()
    ing_purchases = IngredientsPurchase.query.filter_by(purchase_id=id).all()

    ing_purchase = [asdict(ing) for ing in ing_purchases]

    for ing in ing_purchase:
        if ing["ingredient_id"] == ingredient_id:
            return {"detail": "o mesmo ingredient vem sendo comprado mais de uma vez"}, HTTPStatus.BAD_REQUEST

    if not purchase:
        return {"detail": "id not found"}, HTTPStatus.NOT_FOUND
    ingredients_purchase: IngredientsPurchase = IngredientsPurchase(**data)

    setattr(ingredients_purchase, "purchase_id", id)
    setattr(ingredients_purchase, "ingredient_id", ingredient_id)

    db.session.add(ingredients_purchase)
    db.session.commit()

    prueba = IngredientsPurchase.query.filter_by(purchase_id=id).all()
    payload.append(prueba)
    purchase_payload = asdict(purchase)

    purchase_payload.update({"compras": payload})
    return purchase_payload, HTTPStatus.CREATED


@jwt_required()
def ingredients_purchase_loader():
    ingredients_purchase = IngredientsPurchase.query.all()
    return jsonify(ingredients_purchase)

    