from flask import Blueprint
from app.controllers import production_controller

bp_production = Blueprint("productions", __name__, url_prefix="/productions")

bp_production.post("")(production_controller.production_creator)
bp_production.post("/<production_id>")(production_controller.production_recipes_creator)
bp_production.get("")(production_controller.production_loader)
bp_production.get("/intervalo")(production_controller.production_intervaler)
bp_production.patch("")(production_controller.production_updater)
bp_production.delete("")(production_controller.production_deleter)
bp_production.get("/date")(production_controller.production_by_date)
bp_production.get("/<production_id>")(production_controller.production_by_id)
bp_production.patch("/recipes/<production_id>")(production_controller.production_updater)
bp_production.delete("/recipes/<production_id>")(production_controller.production_recipes_deleter)
bp_production.delete("/<production_id>")(production_controller.production_deleter)

bp_production.get("/gamma")(production_controller.gamma)

