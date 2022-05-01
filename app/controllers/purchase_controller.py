from dataclasses import asdict
import re
from flask import jsonify
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from sqlalchemy.orm import Session, Query
from datetime import datetime
from flask import request
from app.models.purchase_model import Purchase
from app.configs.database import db
from app.models.ingredient_model import Ingredient
from app.models.ingredients_purchase_model import IngredientsPurchase
from sqlalchemy import and_


def purchase_creator():
    purchase: Purchase = Purchase()
    db.session.add(purchase)
    db.session.commit()
    return jsonify(purchase)


# @jwt_required()
def purchase_loader():

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

    print(f"{query=}")
    purchases = [purchase._asdict() for purchase in query]

    return jsonify(purchases)


# @jwt_required()
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
            )
            .select_from(Purchase)
            .join(IngredientsPurchase)
            .join(Ingredient)
            # from sqlalchemy import and_
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
    return jsonify(purchases)


def purchase_updater(id):
    data = request.get_json()

    session: Session = db.session

    query: IngredientsPurchase = (
        session.query(IngredientsPurchase).filter_by(id=id).first()
    )
    if not query:
        return {"detail": "id not found"}, 404

    for key, value in data.items():
        setattr(query, key, value)

    session.add(query)
    session.commit()

    return jsonify(query)


# @jwt_required()
def purchase_deleter(id):
    session: Session = db.session

    purchase: IngredientsPurchase = (
        session.query(IngredientsPurchase).filter_by(id=id).first()
    )
    if not purchase:
        return {"detail": "id not found"}, 404

    session.delete(purchase)
    session.commit()

    return "", 204
