from app.configs.database import db
from dataclasses import asdict

def loader(model):
    lista = db.session.query(model).all()
    lista = [asdict(item) for item in lista]
    return lista
