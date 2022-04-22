from flask import Blueprint
from app.controllers import ingredient_controller

bp_ingredient = Blueprint("ingredients", __name__, url_prefix="/ingredients")

bp_ingredient.post("")(ingredient_controller.ingredient_creator)
bp_ingredient.get("")(ingredient_controller.ingredient_loader)
bp_ingredient.patch("")(ingredient_controller.ingredient_updater)
bp_ingredient.delete("")(ingredient_controller.ingredient_deleter)