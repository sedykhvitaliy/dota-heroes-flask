from flask_login import UserMixin

from app import db
from sqlalchemy import ForeignKey




class Heroes(db.Model):
    __tablename__ = "db_heroes"

    id_heroes = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False, unique=True)
    cost = db.Column(db.Integer, nullable=False)
    role = db.Column(db.Integer, nullable=False)
    # image = db.Column(db.String(500))



class Stats(db.Model):
    __tablename__ = "db_stats"

    id_Stats = db.Column(db.Integer, primary_key=True)
    heroes_id = db.Column(db.Integer, ForeignKey("db_heroes.id_heroes"))
    hp = db.Column(db.Integer, nullable=False)
    mana = db.Column(db.Integer, nullable=False)
    damage = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Float, nullable=False)
    distance = db.Column(db.Integer, nullable=False)
    armor = db.Column(db.Integer, nullable=False)
    magic_resistance = db.Column(db.Integer, nullable=False)


class Heroes_info(db.Model):
    __tablename__ = "db_heroes_info"

    id_heroes_info = db.Column(db.Integer, primary_key=True)
    heroes_id = db.Column(db.Integer, ForeignKey("db_heroes.id_heroes"))
    class_heroes = db.Column(db.Integer, nullable=False)
    meta = db.Column(db.Integer, nullable=False)
    is_alliance = db.Column(db.Integer, nullable=False)


class Link(db.Model):
    __tablename__ = "db_links"

    id_links = db.Column(db.Integer, primary_key=True)

class User(db.Model, UserMixin):
    __tablename__ = "db_users"

    email = db.Column(db.String(250), nullable=False, unique=True, primary_key=True)
    password = db.Column(db.String(250), nullable=False)
    administrator = db.Column(db.Boolean, default=False)
    authenticated = db.Column(db.Boolean, default=False)

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated