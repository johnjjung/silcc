"""The application's model objects"""
from silcc.model.meta import Session, Base

import sqlalchemy as sa
from sqlalchemy import orm

from silcc.model import meta
from silcc.model.place import Place

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
    places_table = sa.Table('places', meta.metadata, autoload=True, autoload_with=engine)
    Place.table = places_table
    orm.mapper(Place, Place.table)