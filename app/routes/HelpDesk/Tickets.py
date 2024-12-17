from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.services.HelpDesk.Tickets.tickets_service import *

verTickets_bp = Blueprint('verTickets', __name__)
actTicket_bp = Blueprint('actTicket', __name__)
verTicketID_bp = Blueprint('verTicketID', __name__)
avanzaTicket_bp = Blueprint('avanzaTicket', __name__)
reasignarTicket_bp = Blueprint('reasignarTicket',__name__)
actComentario_bp = Blueprint('actComentario', __name__)
verComentariosID_bp = Blueprint('verComentariosID', __name__)
cancelarTicket_bp = Blueprint('cancelarTicket', __name__)

@verTickets_bp.route('/HelpDesk/verTickets', methods=['POST'])
@jwt_required()
def verTickets_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    user_response = verTickets(data)
    
    return user_response

@actTicket_bp.route('/HelpDesk/actTickets', methods=['POST'])
@jwt_required()
def actTicket_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    user_response = actTicket(data)

    return user_response

@verTicketID_bp.route('/HelpDesk/verTicketID', methods=['GET'])
@jwt_required()
def verTicketID_route():
    ID = request.args.get('ID')

    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response = verTicketID(ID)

    return response

@avanzaTicket_bp.route('/HelpDesk/avanzaTicket', methods=['POST'])
@jwt_required()
def avanzaTicket_route():
    data = request.json
    
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    user_response = avanzaTicket(data)
    
    return user_response

@reasignarTicket_bp.route('/HelpDesk/reasignarTicket', methods=['POST'])
@jwt_required()
def reasignarTicket_route():
    data = request.json
    
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    user_response = reasignarTicket(data)
    
    return user_response

@actComentario_bp.route('/HelpDesk/actComentario', methods=['POST'])
@jwt_required()
def actComentario_route():
    data = request.json
    
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    user_response = actComentario(data)
    
    return user_response

@verComentariosID_bp.route('/HelpDesk/verComentarios', methods=['POST'])
@jwt_required()
def verComentariosID_route():
    data = request.json
    
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    user_response = verComentariosID(data)
    
    return user_response

@cancelarTicket_bp.route('/HelpDesk/cancelarTicket', methods=['POST'])
@jwt_required()
def cancelarTicket_route():
    data = request.json
    
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    user_response = cancelarTicket(data)
    
    return user_response
