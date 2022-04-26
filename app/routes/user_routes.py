from flask import Blueprint
from app.controllers import user_controller

bp_user = Blueprint("users", __name__, url_prefix="/users")

bp_user.post("signup")(user_controller.create_user)
bp_user.post("signin")(user_controller.loger_user)
bp_user.get("")(user_controller.get_user)
bp_user.put("")(user_controller.update_user)
bp_user.delete("")(user_controller.delete_user)

