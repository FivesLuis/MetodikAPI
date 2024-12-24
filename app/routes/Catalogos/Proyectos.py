from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Proyectos.proyectos_service import *

verProyectos_bp = Blueprint('verProyectos',__name__)
verProyectoID_bp = Blueprint('verProyectoID',__name__)
actProyecto_bp = Blueprint('actProyecto',__name__)

@verProyectos_bp.route('/Catalogos/verProyectos', methods=['POST'])
@jwt_required()
def verProyectos_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    user_response = verProyectos(data)
    
    return user_response

@actProyecto_bp.route('/Catalogos/actProyecto', methods=['POST'])
@jwt_required()
def actProyecto_route():
    data = request.json
    
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    user_response = actProyecto(data)
    
    return user_response

@verProyectoID_bp.route('/Catalogos/verProyectoID', methods=['GET'])
@jwt_required()
def verProyectoID_route():
    ID = request.args.get('ID')
    
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response = verProyectoID(ID)
    
    return response