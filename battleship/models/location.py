from . import db


class BoardLocationModel(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    location_x = db.Column(db.SmallInteger, nullable=False)
    location_y = db.Column(db.SmallInteger, nullable=False)
    hit = db.Column(db.Boolean, default=False, index=True)

    ship_id = db.Column(db.Integer, db.ForeignKey('ships.id'))

    def __init__(self, location_x, location_y):
        self.location_x = location_x
        self.location_y = location_y

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def get_co_ordinates(self):
        return (self.location_x, self.location_y)