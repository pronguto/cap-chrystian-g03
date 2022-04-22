from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
)

# def production_creator():
    # return {"msg": "production creator"}

@jwt_required()
def production_loader():
    return {"msg": "production loader"}

@jwt_required()
def production_intervaler():
    return {"msg": "production intervaler"}

# def production_by_date():
#     return {"msg": "production by date"}

@jwt_required()
def production_updater():
    return {"msg": "production updater"}

@jwt_required()
def production_deleter():
    return {"msg": "production deleter"}