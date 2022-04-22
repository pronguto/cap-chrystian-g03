from flask import Blueprint
from app.controllers import recipe_controller

bp_recipe = Blueprint("recipes", __name__, url_prefix="/recipes")

bp_recipe.post("")(recipe_controller.recipe_creator)
bp_recipe.get("")(recipe_controller.recipe_loader)
bp_recipe.patch("")(recipe_controller.recipe_updater)
bp_recipe.delete("")(recipe_controller.recipe_deleter)