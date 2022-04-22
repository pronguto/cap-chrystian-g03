from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
)

@jwt_required()
def recipe_creator():
    return {"msg": "recipe creator"}

@jwt_required()
def recipe_loader():
    return {"msg": "recipe loader"}

@jwt_required()
def recipe_by_name():
    return {"msg": "recipe by name"}

@jwt_required()
def recipe_updater():
    return {"msg": "recipe updater"}

@jwt_required()
def recipe_deleter():
    return {"msg": "recipe deleter"}