from flask import Blueprint
from app.controllers import ingredient_controller

bp_ingredient = Blueprint("ingredients", __name__, url_prefix="/ingredients")

bp_ingredient.post("")(ingredient_controller.ingredient_creator)
bp_ingredient.get("")(ingredient_controller.ingredient_loader)
bp_ingredient.get("/<name>")(ingredient_controller.ingredient_by_name)
bp_ingredient.patch("")(ingredient_controller.ingredient_updater)
bp_ingredient.delete("/<name>")(ingredient_controller.ingredient_deleter)