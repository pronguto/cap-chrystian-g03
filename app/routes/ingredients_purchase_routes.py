from flask import Blueprint
from app.controllers import ingredients_purchase_controller

bp_ipurchase = Blueprint("ingredients_purchase", __name__, url_prefix="")

bp_ipurchase.post("/purchases/<int:id>")(
    ingredients_purchase_controller.ingredients_purchase_creator
)
bp_ipurchase.get("/ingredients_purchase")(
    ingredients_purchase_controller.ingredients_purchase_loader
)
