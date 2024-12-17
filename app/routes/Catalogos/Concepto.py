from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Concepto.concepto_service import (verConceptos, actConcepto, verConceptoID)

verConceptos_bp = Blueprint('verConceptos', __name__)
actConcepto_bp = Blueprint('actConcepto', __name__)
verConceptoID_bp = Blueprint('verConceptoID', __name__)

@verConceptos_bp.route('/Catalogos/verConceptos', methods=['POST'])
@jwt_required()
def conceptos_route():
    data= request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    user_response = verConceptos(data)
    
    return user_response

@actConcepto_bp.route('/Catalogos/actConcepto', methods=['POST'])
@jwt_required()
def actConcepto_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    user_response = actConcepto(data)

    return user_response

@verConceptoID_bp.route('/Catalogos/verConceptoID', methods=['GET'])
@jwt_required()
def verConceptoID_route():
    ID = request.args.get('ID')

    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response = verConceptoID(ID)
    return response