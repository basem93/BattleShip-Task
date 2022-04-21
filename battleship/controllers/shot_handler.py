from battleship.models.location import BoardLocationModel
from battleship.models.ship import ShipModel


class ShotHandler:

    def __init__(self, coordinates):
        self.coordinates = coordinates

    # def create_game_record(self):
    #     game = GameModel(len(self.payload))
    #     game.save_to_db()

    def get_shot(self):
        # get current shot location
        location = None
        try:
            location = BoardLocationModel.query.filter_by\
            (location_x=self.coordinates['x'], location_y=self.coordinates['y']).first()
        except Exception as e:
            pass
        return location

    def update_shot(self):
        location = None
        try:
            location = BoardLocationModel.query.filter_by \
                (location_x=self.coordinates['x'], location_y=self.coordinates['y']).first()
        except Exception as e:
            pass

        if location:
            location.hit = True
            location.update_to_db()
            return True
        return False

    def is_ship_sinked(self, ship_id):
        ship_locations = ShipModel.query.get(int(ship_id)).locations
        for ship in ship_locations:
            if not ship.hit:
                return False
        return True

    def check_shot_location_over_game_borders(self, position_x, position_y):
        return position_x < 0 or position_x > 9 or position_y < 0 or position_y > 9

