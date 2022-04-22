from flask import Flask, Blueprint
from .user_routes import bp_user
from .purchase_routes import bp_purchase
from .recipe_routes import bp_recipe
from .ingredient_routes import bp_ingredient
from .production_routes import bp_production
from .stock_routes import bp_stock

bp_api = Blueprint("api", __name__, url_prefix="/api")

def init_app(app: Flask):
    bp_api.register_blueprint(bp_user)
    bp_api.register_blueprint(bp_purchase)
    bp_api.register_blueprint(bp_ingredient)
    bp_api.register_blueprint(bp_recipe)
    bp_api.register_blueprint(bp_production)
    bp_api.register_blueprint(bp_stock)
    app.register_blueprint(bp_api)