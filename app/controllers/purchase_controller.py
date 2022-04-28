from flask import jsonify
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
)

from app.models.purchase_model import Purchase
from app.configs.database import db

def purchase_creator():
    purchase: Purchase = Purchase()
    db.session.add(purchase)
    db.session.commit()
    return  jsonify(purchase)

# @jwt_required()
def purchase_loader():
    purchases = Purchase.query.all()
    return jsonify(purchases)

@jwt_required()
def purchase_intervaler():
    return {"msg": "purchase intervaler"}

# def purchase_by_date():
#     return {"msg": "purchase by date"}

@jwt_required()
def purchase_updater():
    return {"msg": "purchase updater"}

@jwt_required()
def purchase_deleter():
    return {"msg": "purchase deleter"}