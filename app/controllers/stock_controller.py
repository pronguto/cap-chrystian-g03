from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
)

@jwt_required()
def stock():
    return {"msg": "stock"}