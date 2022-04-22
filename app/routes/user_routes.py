from flask import Blueprint
from app.controllers import user_controller

bp_user = Blueprint("users", __name__, url_prefix="/users")

bp_user.post("/signup")(user_controller.user_creator)
bp_user.post("/signin")(user_controller.user_loger)