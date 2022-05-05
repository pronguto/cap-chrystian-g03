from dataclasses import asdict
import re
from http import HTTPStatus
from flask import jsonify, request
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from sqlalchemy.orm import Session, Query
from datetime import datetime
from app.models.production_recipes_model import ProductionRecipe
from app.models.purchase_model import Purchase
from app.models.ingredients_purchase_model import IngredientsPurchase
from app.models.ingredient_model import Ingredient
from app.models.production_model import Production
from app.models.recipe_model import Recipe
from app.configs.database import db
from sqlalchemy import and_
from app.services.query_services import loader


@jwt_required()
def purchase_creator():
    purchase: Purchase = Purchase()
    db.session.add(purchase)
    db.session.commit()
    return jsonify(purchase), HTTPStatus.CREATED


@jwt_required()
def purchase_loader():
    ingredients = db.session.query(Ingredient).all()
    ingredients = [asdict(ingredient) for ingredient in ingredients]
    purchases = db.session.query(Purchase).all()
    purchases = [asdict(purchase) for purchase in purchases]
    ingredient_purchases = db.session.query(IngredientsPurchase).all()
    ingredient_purchases = [
        asdict(ingredient_purchase) for ingredient_purchase in ingredient_purchases
    ]
    list_purchase = []
    for purchase in purchases:
        purchase["price_total"] = 0
        purchase["Purchases"] = []
        for ingredient_purchase in ingredient_purchases:                       
            if ingredient_purchase["purchase_id"] == purchase["purchase_id"]:
                purchase["Purchases"].append(ingredient_purchase)
            for ingredient in ingredients:
                if ingredient["ingredient_id"] == ingredient_purchase["ingredient_id"]:
                    ingredient_purchase.update(
                        {"ingredient_name": ingredient["ingredient_name"]}
                    )
        for price in purchase["Purchases"]:
            purchase["price_total"] += price["purchase_price"]

        list_purchase.append(purchase)

    return jsonify(list_purchase), HTTPStatus.OK


@jwt_required()
# @jwt_required()
def purchases_loader():


    session: Session = db.session

    """
    select 
        "ingredient_name" ingredients,
        "measurement_unit" ingredients,	
        "purchase_quantity" ingredients_purchase,
        "purchase_price" ingredients_purchase,
        "purchase_date" purchases
    from ingredients ing
    join ingredients_purchase ip 
	    on ing.ingredient_id = ip.ingredient_id 
    join purchases purch
	    on purch.purchase_id = ip.purchase_id 

    """

    query: Query = (
        session.query(
            Ingredient.ingredient_name,
            Purchase.purchase_id,
            Ingredient.ingredient_id,
            Ingredient.measurement_unit,
            IngredientsPurchase.purchase_quantity,
            IngredientsPurchase.purchase_price,
            Purchase.purchase_date,
        )
        .select_from(Purchase)
        .join(IngredientsPurchase)
        .join(Ingredient)
        .all()
    )

    purchases = [purchase._asdict() for purchase in query]

    return jsonify(purchases)

def gustavo_challenge():
    purchases = loader(Purchase)
    compras = loader(IngredientsPurchase)
    ingredientes = loader(Ingredient)

    data = request.args
    initial_date = datetime.strptime(data["initial_date"],"%d-%m-%Y").date()
    final_date = datetime.strptime(data["final_date"], "%d-%m-%Y").date()
    
    lista_de_compras = []
    for purchase in purchases:
        purchase["purchase"] = []
        total_list = []
        if purchase["purchase_date"] > initial_date and purchase["purchase_date"] < final_date:
            for compra in compras:
                if purchase["purchase_id"] == compra["purchase_id"]:
                    purchase["purchase"].append(compra)
                    total_list.append(compra["purchase_price"])
                    for ingrediente in ingredientes:
                        if compra["ingredient_id"] == ingrediente["ingredient_id"]:
                            compra.update({"ingredient_name": ingrediente["ingredient_name"]})
        purchase["purchase_total"] = sum(total_list)
        lista_de_compras.append(purchase)

    return jsonify(lista_de_compras)

def purchase_intervaler():
    session: Session = db.session

    try:
        data = request.args
        initial_date = datetime.strptime(data["initial_date"], "%d-%m-%Y").date()
        final_date = datetime.strptime(data["final_date"], "%d-%m-%Y").date()
        query: Query = (
            session.query(
                Purchase.purchase_id,
                Purchase.purchase_date,
                Ingredient.ingredient_id,
                Ingredient.ingredient_name,
                IngredientsPurchase.purchase_quantity,
                IngredientsPurchase.purchase_price,
                IngredientsPurchase.id,
            )
            .select_from(Purchase)
            .join(IngredientsPurchase)
            .join(Ingredient)
            .filter(
                and_(
                    Purchase.purchase_date > initial_date,
                    Purchase.purchase_date < final_date,
                )
            )
            .order_by(Purchase.purchase_id)
            .all()
        )
    except ValueError:
        return {"detail": "start date or end date is not valid"}, 404

 
    purchases = [purchase._asdict() for purchase in query]
    
    return jsonify(purchases), HTTPStatus.OK

@jwt_required()
def purchase_updater(id):
    data = request.get_json()

    session: Session = db.session
   
    query: IngredientsPurchase = (
        session.query(IngredientsPurchase).filter_by(purchase_id=id).first()
    )
    if not query:
        return {"detail": "id not found"}, 404

    for key, value in data.items():
        setattr(query, key, value)

    session.add(query)
    session.commit()

    return jsonify(query)


@jwt_required()
def purchase_deleter(id):
    session: Session = db.session

    purchase: Purchase = (
        session.query(Purchase).filter_by(purchase_id=id).first()
    )
    if not purchase:
        return {"detail": "id not found"}, 404

    session.delete(purchase)
    session.commit()
    return "", 204

def alfa():
    purchases = loader(Purchase)
    compras = loader(IngredientsPurchase)

    lista_de_compras = []
    for purchase in purchases:
        total_list = []
        for compra in compras:
            if purchase["purchase_id"] == compra["purchase_id"]:
                total_list.append(compra["purchase_price"])
        purchase["purchase_total"] = sum(total_list)
        lista_de_compras.append(purchase)

    return jsonify(lista_de_compras)