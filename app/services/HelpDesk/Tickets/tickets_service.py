from app.procedures.HelpDesk.Tickets.tickets_procedures import *

def verTickets(data):
    return ver_Tickets(data)

def actTicket(data):
    return act_Ticket(data)

def verTicketID(ID):
    return ver_TicketID(ID)

def avanzaTicket(data):
    return avanza_Ticket(data)

def reasignarTicket(data):
    return reasignar_Ticket(data)

def actComentario(data):
    return act_Comentario(data)

def verComentariosID(data):
    return ver_ComentariosID(data)

def cancelarTicket(data):
    return cancel_Ticket(data)