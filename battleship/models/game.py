from datetime import datetime

from . import db
from .ship import ShipModel


class GameModel(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    number_of_ships = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    ships = db.relationship('ShipModel', backref='game')

    def __init__(self, number_of_ships):
        self.name = "battleship"
        self.number_of_ships = number_of_ships

    def get_number_of_ships(self):
        return self.number_of_ships

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()