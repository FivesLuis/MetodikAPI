from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Comercial.Reservas.reservasD_service import *

verReservaID_bp = Blueprint('verReservaID', __name__)
avanzaReserva_bp = Blueprint('avanzaReserva', __name__)
verViajesDisponibles_bp = Blueprint('verViajesDisponibles', __name__)
verViajesDisponiblesVuelta_bp = Blueprint('verViajesDisponiblesVuelta', __name__)
actReservaD_bp = Blueprint('ActReservaD', __name__)
verReservaDetalle_bp = Blueprint('VerReservaDetalle', __name__)
eliminarRenglonReserva_bp = Blueprint('EliminarRenglonReserva', __name__)
afectarReserva_bp = Blueprint('afectarReserva', __name__)
cancelarReserva_bp = Blueprint('cancelarReserva', __name__)
verAsientosDispoblesRuta_bp = Blueprint('verAsientosDispoblesRuta', __name__)
agregarAsientosReserva_bp = Blueprint('agregarAsientosReserva', __name__)
guardarDatosPersonasReserva_bp = Blueprint('guardarDatosPersonasReserva', __name__)
verPersonasReserva_bp = Blueprint('verPersonasReserva', __name__)
agregarFormaPagoReserva_bp = Blueprint('agregarFormaPagoReserva', __name__)
cambiarSituacion_bp = Blueprint('cambiarSituacion', __name__)



@verReservaID_bp.route('/Comercial/Reservas/verReservaID', methods=['GET'])
@jwt_required()
def usuarios_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verReservaID(ID)
    return response


@avanzaReserva_bp.route('/Comercial/Reservas/avanzarReserva', methods=['POST'])
@jwt_required()
def nvaReserva_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = avanzaReserva(data)
    return response

@verViajesDisponibles_bp.route('/Comercial/Reservas/verViajesDisponiblesIda', methods=['GET'])
@jwt_required()
def verViajesDisponibles_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verViajesDisponibles(ID)
    return response


@verViajesDisponiblesVuelta_bp.route('/Comercial/Reservas/verViajesDisponiblesVuelta', methods=['GET'])
@jwt_required()
def verViajesDisponiblesVuelta_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verViajesDisponiblesVuelta(ID)
    return response

@actReservaD_bp.route('/Comercial/Reservas/ActReservaD', methods=['POST'])
@jwt_required()
def actReservaD_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = ActReservaD(data)
    return response

@verReservaDetalle_bp.route('/Comercial/Reservas/verReservaDetalle', methods=['GET'])
@jwt_required()
def verReservaDetalle_route():
    ID = request.args.get('ID')
    print(ID)
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = VerReservaDetalle(ID)
    return response

@eliminarRenglonReserva_bp.route('/Comercial/Reservas/eliminarRenglonReserva', methods=['DELETE'])
@jwt_required()
def eliminarRenglonReserva_route():
    ID = request.args.get('ID')
    RenglonID = request.args.get('RenglonID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = EliminarRenglonReserva(ID, RenglonID)
    return response

@afectarReserva_bp.route('/Comercial/Reservas/afectarReserva', methods=['POST'])
@jwt_required()
def afectarReserva_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = afectarReserva(data)
    return response

@cancelarReserva_bp.route('/Comercial/Reservas/cancelarReserva', methods=['POST'])
@jwt_required()
def cancelarReserva_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = cancelarReserva(data)
    return response

@verAsientosDispoblesRuta_bp.route('/Comercial/Reservas/verAsientosDispoblesRuta', methods=['POST'])
@jwt_required()
def verAsientosDispoblesRuta_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verAsientosDispoblesRuta(data)
    return response

@agregarAsientosReserva_bp.route('/Comercial/Reservas/agregarAsientos', methods=['POST'])
@jwt_required()
def agregarAsientosReserva_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = agregarAsientosReserva(data)
    return response

@guardarDatosPersonasReserva_bp.route('/Comercial/Reservas/guardarDatosPersona', methods=['POST'])
@jwt_required()
def guardarDatosPersonasReserva_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = guardarDatosPersonasReserva(data)
    return response

@verPersonasReserva_bp.route('/Comercial/Reservas/verPersonasReserva', methods=['GET'])
@jwt_required()
def verPersonasReserva_route():
    ID = request.args.get('ID')
    HorarioRutaID = request.args.get('HorarioRutaID')
    RenglonID = request.args.get('RenglonID')

    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verPersonasReserva(ID, HorarioRutaID, RenglonID)
    return response

@agregarFormaPagoReserva_bp.route('/Comercial/Reservas/agregarPagoReserva', methods=['POST'])
@jwt_required()
def gregarFormaPagoReserva_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = agregarFormaPagoReserva(data)
    return response

@cambiarSituacion_bp.route('/Comercial/Reservas/cambiarSituacion', methods=['POST'])
@jwt_required()
def cambiarSituacion_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = cambiarSituacion(data)
    return response