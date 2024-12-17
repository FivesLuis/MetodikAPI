from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Areas.areas_service import *

verAreas_bp = Blueprint('verAreas', __name__)
actArea_bp = Blueprint('actArea', __name__)
verAreaID_bp = Blueprint('verAreaID', __name__)

@verAreas_bp.route('/Catalogos/verAreas', methods=['POST'])
@jwt_required()
def areas_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    user_response = verAreas(data)

    return user_response

@actArea_bp.route('/Catalogos/actArea', methods=['POST'])
@jwt_required()
def actArea_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    user_response = actArea(data)

    return user_response

@verAreaID_bp.route('/Catalogos/verAreaID', methods=['GET'])
@jwt_required()
def verAreaID_route():
    ID = request.args.get('ID')

    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response = verAreaID(ID)

    return response
