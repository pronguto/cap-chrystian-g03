from flask import Blueprint
from app.controllers import ingredients_purchase_controller

bp_ipurchase = Blueprint("ingredients_purchase", __name__, url_prefix="")

bp_ipurchase.post("/purchases/<int:id>")(
    ingredients_purchase_controller.ingredients_purchase_creator
)
bp_ipurchase.get("/ingredients_purchase")(
    ingredients_purchase_controller.ingredients_purchase_loader
)
# bp_ipurchase.get("/intervalo")(ingredients_purchase_controller.purchase_intervaler)
# bp_ipurchase.patch("")(ingredients_purchase_controller.purchase_updater)
# bp_ipurchase.delete("")(ingredients_purchase_controller.purchase_deleter)
