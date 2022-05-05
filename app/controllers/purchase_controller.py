from dataclasses import asdict
from http import HTTPStatus
from flask import jsonify
from flask_jwt_extended import jwt_required
from sqlalchemy.orm import Session, Query
from datetime import datetime
from flask import request
from app.models.purchase_model import Purchase
from app.configs.database import db
from app.models.ingredient_model import Ingredient
from app.models.ingredients_purchase_model import IngredientsPurchase
from app.services import ingredient_service
from app.models.exceptions.ingredient_exception import KeysError
from sqlalchemy.orm.exc import StaleDataError
from sqlalchemy import and_


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
