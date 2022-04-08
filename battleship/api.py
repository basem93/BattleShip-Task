from http import HTTPStatus

from flask import Flask, jsonify, request

# import battleship.controllers.end_game_handeler as end_game_handeler
# import battleship.controllers.shot_handeler as shot_handeler


app = Flask(__name__)

from battleship.controllers.game_creator_handler import StartGameHandler
from battleship.controllers.database_handler import delete_all_database_records


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
    return jsonify({}), HTTPStatus.NOT_IMPLEMENTED


@app.route('/battleship', methods=['DELETE'])
def delete_battleship_game():
    return jsonify({}), HTTPStatus.NOT_IMPLEMENTED
