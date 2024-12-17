from app.utils.db_helpers import execute_stored_procedure

def ver_Tickets(data):
    sp_name = "spVerTickets"
    params = [
        data.get("EmpresaID"),
        data.get("EstatusID"),
        data.get("PersonaID"),
        data.get("AreaID"),
        data.get("Prioridad"),
        data.get("FechaD"),
        data.get("FechaH")
    ]
    return execute_stored_procedure(sp_name, params)

def act_Ticket(data):
    sp_name = "spActTicket"
    params = [
        data.get("ID"),
        data.get("EstatusID"),
        data.get("Prioridad"),
        data.get("ConceptoID"),
        data.get("AreaID"),
        data.get("Nombre"),
        data.get("Descripcion"),
        data.get("RutaArchivo"),
        data.get("PersonaID"),
        data.get("EmpresaID")
    ]
    return execute_stored_procedure(sp_name, params)

def ver_TicketID(ID):
    sp_name = "spVerTicketID"
    params = [ID]
    return execute_stored_procedure(sp_name, params)

def avanza_Ticket(data):
    sp_name = "spAvanzaTicket"
    params = [
        data.get("ID"),
        data.get("EstatusID"),
        data.get("PersonaID")
    ]
    return execute_stored_procedure(sp_name, params)

def reasignar_Ticket(data):
    sp_name = "spReasignarTicket"
    params = [
        data.get("ID"),
        data.get("PersonaID")
    ]
    return execute_stored_procedure(sp_name, params)

def act_Comentario(data):
    sp_name = "spActComentarioTicked"
    params = [
        data.get("ID"),
        data.get("Comentario"),
        data.get("TicketID"),
        data.get("RutaArchivo"),
        data.get("PersonaID"),
        data.get("EmpresaID")
    ]
    return execute_stored_procedure(sp_name, params)

def ver_ComentariosID(data):
    sp_name = "spVerComentariosTicket"
    params = [
        data.get("ID"), 
        data.get("EmpresaID")
    ]
    return execute_stored_procedure(sp_name, params)

def cancel_Ticket(data):
    sp_name = "spCancelarTicket"
    params = [
        data.get("ID"),
        data.get("PersonaID"),
    ]
    return execute_stored_procedure(sp_name, params)
