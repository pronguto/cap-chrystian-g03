from flask import Blueprint
from app.controllers import purchase_controller

bp_purchase = Blueprint("purchases", __name__, url_prefix="/purchases")

bp_purchase.post("")(purchase_controller.purchase_creator)
bp_purchase.get("")(purchase_controller.purchase_loader)
bp_purchase.get("/burt")(purchase_controller.burt)
bp_purchase.get("/")(purchase_controller.purchase_intervaler)
# bp_purchase.patch("/<id>")(purchase_controller.purchase_updater)
bp_purchase.delete("")(purchase_controller.purchase_deleter)
bp_purchase.get("/production")(purchase_controller.production_loader)
