from datetime import timedelta
from http import HTTPStatus

from app.configs.database import db
from app.models.user_model import User
from flask import jsonify, request
from flask_jwt_extended import (create_access_token, get_jwt_identity,
                                jwt_required)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session
from werkzeug.security import generate_password_hash


def create_user():
    data = request.get_json()
    try:
        user: User = User(**data)
        db.session.add(user)
        db.session.commit()
        return jsonify(user), HTTPStatus.CREATED
    except (TypeError, KeyError, NameError):
        return {"Error": "Incorrect format key"}, HTTPStatus.BAD_REQUEST
    except IntegrityError:
        return {"error": "User already exists"}, HTTPStatus.BAD_REQUEST
    
def loger_user():
    data = request.get_json()
    session: Session = db.session
    try:
        email = data["email"]
        password = data["password"]
        query =  session.query(User)
        user_by_email = query.filter(User.email == email).first()   
        if not user_by_email:
            return {"Error": "User not found"}, HTTPStatus.NOT_FOUND
        allowed = user_by_email.check_password(password)
        if not allowed:
            return {"Error": "Invalid password"}, HTTPStatus.NOT_FOUND
        output_token = create_access_token(user_by_email, expires_delta=timedelta(minutes=30))
        return {"access_token": output_token}
    except KeyError:
        return {"Error": "Incorrect format key"}, HTTPStatus.BAD_REQUEST

@jwt_required()
def get_user():
    current_user = get_jwt_identity()
    return jsonify(current_user), HTTPStatus.OK

@jwt_required()
def update_user():
    data = request.get_json()
    session: Session = db.session
    try:
        email = data["email"]
        name = data["name"]
        password = data["password"]    
        patch_user = session.query(User).filter(User.email == email).update({
            User.name: name,
            User.password_hash: generate_password_hash(password)
        })   
        if not patch_user:
            return {"Error": "Email not found"}, HTTPStatus.NOT_FOUND
        session.commit()
        output_user= session.query(User).filter_by(name= name).first()
        return jsonify(output_user), HTTPStatus.OK
    except KeyError:
        return {"Error": "Incorrect format key"}, HTTPStatus.BAD_REQUEST

@jwt_required()
def delete_user():
    session: Session = db.session
    current_user = get_jwt_identity()
    email = current_user["email"]
    output_delete_user = session.query(User).filter(User.email == email).first()   
    if not output_delete_user:
        return {"Error": "Email not found"}, HTTPStatus.NOT_FOUND
    output_message = {
        "message": f"User {output_delete_user.name} has been deleted."
    }
    session.delete(output_delete_user)
    session.commit()
    return jsonify(output_message), HTTPStatus.OK

    