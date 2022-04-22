from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
)

@jwt_required()
def ingredient_creator():
    return {"msg": "ingredient creator"}

@jwt_required()
def ingredient_loader():
    return {"msg": "ingredient loader"}

# def ingredient_by_name():
#     return {"msg": "ingredient by name"}

@jwt_required()
def ingredient_updater():
    return {"msg": "ingredient updater"}

@jwt_required()
def ingredient_deleter():
    return {"msg": "ingredient deleter"}