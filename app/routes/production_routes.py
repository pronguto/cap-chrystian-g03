from flask import Blueprint
from app.controllers import production_controller

bp_production = Blueprint("productions", __name__, url_prefix="/productions")

bp_production.get("")(production_controller.production_loader)
bp_production.get("/intervalo")(production_controller.production_intervaler)
bp_production.patch("")(production_controller.production_updater)
bp_production.delete("")(production_controller.production_deleter)