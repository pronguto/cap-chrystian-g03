from flask import Blueprint
from app.controllers import purchase_controller

bp_purchase = Blueprint("purchases", __name__, url_prefix="/purchases")

bp_purchase.get("")(purchase_controller.purchase_loader)
bp_purchase.get("/intervalo")(purchase_controller.purchase_intervaler)
bp_purchase.patch("")(purchase_controller.purchase_updater)
bp_purchase.delete("")(purchase_controller.purchase_deleter)