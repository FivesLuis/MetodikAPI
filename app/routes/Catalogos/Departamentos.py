from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Departamentos.departamentos_service import *

verDepartamentos_bp = Blueprint('verDepartamentos', __name__)
verDepartamentoID_bp = Blueprint('verDepartamentosID', __name__)
actDepartamento_bp = Blueprint('actDepartamentos', __name__)

@verDepartamentos_bp.route('/Catalogos/verDepartamentos', methods=['POST'])
@jwt_required()
def departamentos_route():
    data = request.json
    
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    user_response = verDepartamentos(data)
    
    return user_response

@actDepartamento_bp.route('/Catalogos/actDepartamento', methods=['POST'])
@jwt_required()
def actDepartamento_route():
    data = request.json
    
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    user_response = actDepartamento(data)
    
    return user_response

@verDepartamentoID_bp.route('/Catalogos/verDepartamentoID', methods=['GET'])
@jwt_required()
def departamentoID_route():
    ID = request.args.get('ID')
    
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    response = verDepartamentoID(ID)
    
    return response