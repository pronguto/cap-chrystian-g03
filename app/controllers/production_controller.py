from datetime import datetime
from dataclasses import asdict
from http import HTTPStatus
from turtle import update
from flask import jsonify, request, session
from sqlalchemy.orm import Query, Session
from app.models.exceptions.ingredient_exception import KeysError
from app.models.production_model import Production
from app.models.production_recipes_model import ProductionRecipe
from app.models.recipe_model import Recipe
from app.services.query_services import loader
from app.configs.database import db
from sqlalchemy import and_
from sqlalchemy.exc import IntegrityError, DataError
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
)

from app.services import ingredient_service

#@jwt_required()
def production_creator():
    session: Session = db.session

    product: Production = Production()
    session.add(product)
    session.commit()


    return jsonify(product), HTTPStatus.CREATED

#@jwt_required()
def production_recipes_creator(production_id):
    session: Session = db.session
    data = request.get_json()

    expected_keys={"recipe_id","recipe_quantity"}
    try:
        ingredient_service.validate_keys(body_request=data, expected_keys= expected_keys)
    except KeysError as e:
        return e.message, e.status_code

    data["production_id"]=int(production_id)
    productionrecipe = ProductionRecipe(**data)

    try:
        session.add(productionrecipe)
        session.commit()
    except IntegrityError:
        return {"msg":"recipe_id no existent"}, HTTPStatus.BAD_REQUEST
    except DataError:
        return {"msg":"values invalid", "exeple":{
		"recipe_id":1,
	 	"recipe_quantity":1.5
	}}

    return jsonify(productionrecipe), HTTPStatus.CREATED

#@jwt_required()
def production_loader():

    session: Session = db.session

    Productions: Query= session.query(Production).all()
    sezalized_production= []
    for production in Productions:
        base_query_productionsRicipes: Query= session.query(
            ProductionRecipe.id, 
            ProductionRecipe.recipe_id, 
            ProductionRecipe.recipe_quantity,
            ProductionRecipe.production_id
        ).filter_by(production_id= production.production_id).all()
        production_ricipe_id=[]
        for productions_ricipe in base_query_productionsRicipes:
            production_ricipe_id.append(productions_ricipe)
        to_seralize_production=[]
        for production_id in production_ricipe_id:
            production_ricipe= {
            "id": production_id[0],
            "recipe_id": production_id[1],
            "recipe_quantity": production_id[2],
            "production_id": production_id[3],
            }
            to_seralize_production.append(production_ricipe)
        seralize_production= {"recipes": to_seralize_production}
        seralize_production.update(asdict(production))
        sezalized_production.append(seralize_production)

    return jsonify(sezalized_production), HTTPStatus.OK

#@jwt_required()
def production_intervaler():
    session: Session = db.session
    data = request.args
    initial_date = datetime.strptime(data["initial_date"], "%d-%m-%Y").date()
    final_date = datetime.strptime(data["final_date"], "%d-%m-%Y").date()
    
    
    Productions: Query = (
        session.query(Production)
            .select_from(Production)
            .filter(
                and_(
                    Production.production_date >= initial_date,
                    Production.production_date <= final_date,
                )
            )
            .order_by(Production.production_id)
            .all())
    sezalized_production= []
    for production in Productions:
        base_query_productionsRicipes: Query= session.query(
            ProductionRecipe.id, 
            ProductionRecipe.recipe_id, 
            ProductionRecipe.recipe_quantity,
            ProductionRecipe.production_id
        ).filter_by(production_id= production.production_id).all()
        production_ricipe_id=[]
        for productions_ricipe in base_query_productionsRicipes:
            production_ricipe_id.append(productions_ricipe)
        to_seralize_production=[]
        for production_id in production_ricipe_id:
            production_ricipe= {
            "id": production_id[0],
            "recipe_id": production_id[1],
            "recipe_quantity": production_id[2],
            "production_id": production_id[3],
            }
            to_seralize_production.append(production_ricipe)
        seralize_production= {"recipes": to_seralize_production}
        seralize_production.update(asdict(production))
        sezalized_production.append(seralize_production)

    return jsonify(sezalized_production), HTTPStatus.OK

#@jwt_required()
def production_by_date():
    session: Session = db.session
    data = request.args

    date = datetime.strptime(data["date"], "%d-%m-%Y").date()

    Productions: Query = (
        session.query(Production)
            .select_from(Production)
            .filter(
                and_(
                    Production.production_date == date
                )
            )
            .order_by(Production.production_id)
            .all())
    sezalized_production= []
    for production in Productions:
        base_query_productionsRicipes: Query= session.query(
            ProductionRecipe.id, 
            ProductionRecipe.recipe_id, 
            ProductionRecipe.recipe_quantity,
            ProductionRecipe.production_id
        ).filter_by(production_id= production.production_id).all()
        production_ricipe_id=[]
        for productions_ricipe in base_query_productionsRicipes:
            production_ricipe_id.append(productions_ricipe)
        to_seralize_production=[]
        for production_id in production_ricipe_id:
            production_ricipe= {
            "id": production_id[0],
            "recipe_id": production_id[1],
            "recipe_quantity": production_id[2],
            "production_id": production_id[3],
            }
            to_seralize_production.append(production_ricipe)
        seralize_production= {"recipes": to_seralize_production}
        seralize_production.update(asdict(production))
        sezalized_production.append(seralize_production)


    return jsonify(sezalized_production), HTTPStatus.OK

#@jwt_required()
def production_by_id(production_id):
    session: Session = db.session

    Productions: Query = (
        session.query(Production)
            .select_from(Production)
            .filter(
                and_(
                    Production.production_id == production_id
                )
            )
            .order_by(Production.production_id)
            .all())
    sezalized_production= []
    for production in Productions:
        base_query_productionsRicipes: Query= session.query(
            ProductionRecipe.id, 
            ProductionRecipe.recipe_id, 
            ProductionRecipe.recipe_quantity,
            ProductionRecipe.production_id
        ).filter_by(production_id= production.production_id).all()
        production_ricipe_id=[]
        for productions_ricipe in base_query_productionsRicipes:
            production_ricipe_id.append(productions_ricipe)
        to_seralize_production=[]
        for production_id in production_ricipe_id:
            production_ricipe= {
            "id": production_id[0],
            "recipe_id": production_id[1],
            "recipe_quantity": production_id[2],
            "production_id": production_id[3],
            }
            to_seralize_production.append(production_ricipe)
        seralize_production= {"recipes": to_seralize_production}
        seralize_production.update(asdict(production))
        sezalized_production.append(seralize_production)

    if not sezalized_production:
        return {"Error": "id not found"}, HTTPStatus.NOT_FOUND

    return jsonify(sezalized_production), HTTPStatus.OK


#@jwt_required()
def production_updater(production_id):
    data = request.get_json()
    session: Session = db.session

    expected_keys={"recipe_id","recipe_quantity"}
    try:
        ingredient_service.validate_keys(body_request=data, expected_keys= expected_keys)
    except KeysError as e:
        return e.message, e.status_code
    
    try:
        query: Query = (
            session.query(ProductionRecipe)
                .filter(ProductionRecipe.id == production_id
                )).update({
                    ProductionRecipe.recipe_id: data["recipe_id"],
                    ProductionRecipe.recipe_quantity: data["recipe_quantity"]
                })
    except IntegrityError:
        return {"msg":"recipe_id no existent"}, HTTPStatus.BAD_REQUEST
    except DataError:
        return {"msg":"values invalid", "exeple":{
		"recipe_id":1,
	 	"recipe_quantity":1.5
	}}, HTTPStatus.BAD_REQUEST

    productionsrecipe: Query = (
        session.query(Production.production_id, 
            Production.production_date,
            ProductionRecipe.id, 
            ProductionRecipe.recipe_id,
            ProductionRecipe.recipe_quantity)
            .select_from(Production)
            .join(ProductionRecipe)
            .filter(
                and_(
                   ProductionRecipe.id == production_id
                )
            )
            .order_by(Production.production_id)
            .all()
    )
    products = [product._asdict() for product in productionsrecipe]

    if not products:
        return {"Error": "id not found"}, HTTPStatus.BAD_REQUEST
 
    return jsonify(products[0]), HTTPStatus.OK

#@jwt_required()
def production_recipes_deleter(production_id):
    session: Session = db.session()

    productionsrecipe: ProductionRecipe = (
        ProductionRecipe.query.filter_by(id = production_id).first()
    )
    if not productionsrecipe:
        return {"Error": "id not found"}, HTTPStatus.NOT_FOUND
    
    session.delete(productionsrecipe)
    session.commit()
    return "", HTTPStatus.NO_CONTENT

#@jwt_required()
def production_deleter(production_id):
    session: Session = db.session()

    productions: Production = (
        Production.query.filter_by(production_id = production_id).first()
    )
    if not productions:
        return {"Error": "id not found"}, HTTPStatus.NOT_FOUND
    
    session.delete(productions)
    session.commit()
    return "", HTTPStatus.NO_CONTENT

def gamma():
    productions = loader(Production)
    formulas = loader(ProductionRecipe)
    recetas = loader(Recipe)

    lista_de_consumo = []
    for receta in recetas:
        receta["productions"] = []
        total_list = []
        for formula in formulas:
            if receta["recipe_id"] == formula["recipe_id"]:
                receta["productions"].append(formula)
                total_list.append(formula["recipe_quantity"])
            for production in productions:
                if formula["production_id"] == production["production_id"]:
                    formula.update({"production_date": production["production_date"]})
        receta["quantity_total"] = sum(total_list)
        lista_de_consumo.append(receta)

    return jsonify(lista_de_consumo)