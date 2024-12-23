from app.utils.db_helpers import execute_stored_procedure

def ver_Proyectos(data):
    sp_name = "spVerProyectos"
    params = [
        data.get("PersonaID"),
        data.get("EmpresaID"),
        data.get("EstatusID"),
        data.get("FechaD"),
        data.get("FechaH")
    ]
    return execute_stored_procedure(sp_name, params)

def act_Proyectos(data):
    sp_name = "spActProyecto"
    params = [
        data.get("ID"),
        data.get("Nombre"),
        data.get("EstatusID"),
        data.get("EmpresaID"),
        data.get("PersonaID"),
        data.get("Descripcion"),
        data.get("DepartamentoID"),
        data.get("Imagen"),
        data.get("Observaciones"),
        data.get("Correo"),
        data.get("Telefono"),
        data.get("EquipoID"),
        data.get("PerfilID"),
        data.get("Tiempo"),
        data.get("EmpresaCte")
    ]
    return execute_stored_procedure(sp_name, params)

def ver_ProyectoID(ID):
    sp_name = "spVerProyectoID"
    params = [ID]
    return execute_stored_procedure(sp_name, params)