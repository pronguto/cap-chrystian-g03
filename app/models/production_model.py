from dataclasses import dataclass
from datetime import datetime

from app.configs.database import db
from sqlalchemy import Column, Date, Integer


@dataclass
class Production (db.Model):
    production_id: int
    production_date: str

    __tablename__ = "productions"

    production_id = Column(Integer, primary_key = True)
    production_date = Column(Date, default = datetime.now())
    
