from flask import Blueprint, jsonify

wroom_blueprint = Blueprint('users', __name__)

@wroom_blueprint.route('/wroom/ping', methods=['GET'])
def ping_pong():
    return jsonify(
        'status': 'success',
        'message': 'pong!'
    )
