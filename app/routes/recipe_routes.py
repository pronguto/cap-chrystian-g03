from flask import Blueprint
from app.controllers import recipe_controller

bp_recipe = Blueprint("recipes", __name__, url_prefix="/recipes")

bp_recipe.post("")(recipe_controller.create_recipe)
bp_recipe.post("/<int:id>")(recipe_controller.recipe_ingredients_creator)
bp_recipe.get("")(recipe_controller.get_all_recipes)
bp_recipe.get("/<name>")(recipe_controller.get_recipe_by_name)
bp_recipe.patch("")(recipe_controller.patch_recipe)
bp_recipe.delete("/")(recipe_controller.delete_recipe_by_id)
bp_recipe.delete("/<name>")(recipe_controller.delete_recipe)
