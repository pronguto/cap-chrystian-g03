from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
)

# def purchase_creator():
#     return {"msg": "purchase creator"}

@jwt_required()
def purchase_loader():
    return {"msg": "purchase loader"}

@jwt_required()
def purchase_intervaler():
    return {"msg": "purchase intervaler"}

# def purchase_by_date():
#     return {"msg": "purchase by date"}

@jwt_required()
def purchase_updater():
    return {"msg": "purchase updater"}

@jwt_required()
def purchase_deleter():
    return {"msg": "purchase deleter"}