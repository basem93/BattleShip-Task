from http import HTTPStatus

from flask import Flask, jsonify, request

# import battleship.controllers.end_game_handeler as end_game_handeler
# import battleship.controllers.shot_handeler as shot_handeler

app = Flask(__name__)

from battleship.controllers.game_creator_handler import StartGameHandler
from battleship.controllers.database_handler import delete_all_database_records
from battleship.controllers.shot_handler import ShotHandler

@app.route("/")
def hello():
    return "Welcome to BattleShip game."

@app.route('/battleship', methods=['POST'])
def create_battleship_game():
    delete_all_database_records()
    request_data = request.get_json()
    game_creator_handler = StartGameHandler(request_data['ships'])
    game_creator_handler.create_game_record()

    ship_locations_are_correct = game_creator_handler.create_ships()
    if not ship_locations_are_correct:
        return jsonify(message="Please, check request data"), HTTPStatus.BAD_REQUEST

    ship_is_not_overlapped = game_creator_handler.check_overlapped_ships()
    if not ship_is_not_overlapped:
        return jsonify(message="Please, check request data"), HTTPStatus.BAD_REQUEST

    return jsonify(message="Game created successfully"), HTTPStatus.OK


@app.route('/battleship', methods=['PUT'])
def shot():
    request_data = request.get_json()
    shot_handler = ShotHandler(request_data)

    out_of_game_border = shot_handler.check_shot_location_over_game_borders(request_data['x'], request_data['y'])
    if out_of_game_border:
        return jsonify(message="shot falls outside of the board"), HTTPStatus.BAD_REQUEST

    shot_location = shot_handler.get_shot()

    # shot did not hit any ships locations
    if not shot_location:
        return jsonify(result="WATER"), HTTPStatus.OK

    if shot_location.hit:
        return jsonify(result="HIT"), HTTPStatus.OK

    # if shot hit any ship, update hit locaton to True
    shot_handler.update_shot()

    if shot_handler.is_ship_sinked(shot_location.ship_id):
        return jsonify(result="SINK"), HTTPStatus.OK
    else:
        return jsonify(result="HIT"), HTTPStatus.OK


@app.route('/battleship', methods=['DELETE'])
def delete_battleship_game():
    delete_all_database_records()
    return jsonify(message="Game deleted successfully"), HTTPStatus.OK
