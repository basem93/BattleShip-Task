from battleship.models.game import GameModel
from battleship.models.ship import ShipModel
from battleship.models.location import BoardLocationModel


class StartGameHandler:

    def __init__(self, payload):
        self.payload = payload

    def create_game_record(self):
        game = GameModel(len(self.payload))
        game.save_to_db()

    def create_ships(self):
        for ship in self.payload:

            _ship = ShipModel(name="ship_", origin_x=ship['y'], origin_y=ship['y'],
                              size=ship['size'], orientation=ship['direction'])
            _ship.save_to_db()
            ship_locations_are_correct = self._create_ship_locations(ship['x'], ship['y'], ship['size'],
                                                                     ship['direction'])
            if not ship_locations_are_correct:
                return False
        return True

    def _create_ship_locations(self, origin_x, origin_y, size, orientation):
        if orientation == 'H':
            if size % 2 == 0:
                for x in range(int(origin_x - (size + 1) // 2 + 1), int(origin_x + (size + 1) / 2 + 1)):
                    out_of_game_border = self._check_ship_locations_over_game_borders(x, origin_y)
                    if out_of_game_border:
                        return False
                    location = BoardLocationModel(x, origin_y)
                    location.save_to_db()
            else:
                for x in range(int(origin_x - (size + 1) // 2 + 1), int(origin_x + (size + 1) / 2)):
                    out_of_game_border = self._check_ship_locations_over_game_borders(x, origin_y)
                    if out_of_game_border:
                        return False
                    location = BoardLocationModel(x, origin_y)
                    location.save_to_db()
        else:
            if size % 2 == 0:
                for y in range(int(origin_y - (size + 1) // 2 + 1), int(origin_y + (size + 1) / 2 + 1)):
                    out_of_game_border = self._check_ship_locations_over_game_borders(origin_x, y)
                    if out_of_game_border:
                        return False
                    location = BoardLocationModel(origin_x, y)
                    location.save_to_db()
            else:
                for y in range(int(origin_y - (size + 1) // 2 + 1), int(origin_y + (size + 1) / 2)):
                    out_of_game_border = self._check_ship_locations_over_game_borders(origin_x, y)
                    if out_of_game_border:
                        return False
                    location = BoardLocationModel(origin_x, y)
                    location.save_to_db()
        return True

    def _check_ship_locations_over_game_borders(self, position_x, position_y):
        return position_x < 0 or position_x > 9 or position_y < 0 or position_y > 9

    def check_overlapped_ships(self):
        locations = BoardLocationModel.query.all()
        locations_list = [location.get_co_ordinates() for location in locations]
        return len(locations_list) == len(set(locations_list))
