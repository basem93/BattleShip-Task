from . import db
from .location import BoardLocationModel


class ShipModel(db.Model):
    __tablename__ = 'ships'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    origin_x = db.Column(db.SmallInteger, nullable=False)
    origin_y = db.Column(db.SmallInteger, nullable=False)
    size = db.Column(db.SmallInteger, nullable=False)
    orientation = db.Column(db.String(1))
    sink = db.Column(db.Boolean, default=False, index=True)

    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))

    locations = db.relationship('BoardLocationModel', backref='ship')

    def __init__(self, name, origin_x, origin_y, size, orientation):
        self.name = name
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.size = size
        self.orientation = orientation

    def get_ship_size(self):
        return self.size

    def save_to_db(self):
        x = db.session.add(self)
        v = db.session.commit()
        print('cc')

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()