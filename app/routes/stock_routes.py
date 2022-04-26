from flask import Blueprint
from app.controllers import stock_controller

bp_stock = Blueprint("ingredients_purchase", __name__, url_prefix="/stock")

bp_stock.get("")(stock_controller.stock)