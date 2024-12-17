from app.utils.db_helpers import execute_stored_procedure

def ver_Areas(data):
    sp_name = "spVerAreas"
    params = [
        data.get("PersonaID"),
        data.get("EmpresaID"),
        data.get("EstatusID"),
        data.get("FechaD"),
        data.get("FechaH")
    ]
    return execute_stored_procedure(sp_name, params)

def act_Area(data):
    sp_name = "spActAreas"
    params = [
        data.get("ID"),
        data.get("Nombre"),
        data.get("EstatusID"),
        data.get("Descripcion"),
        data.get("PersonaID"),
        data.get("EmpresaID")
    ]
    return execute_stored_procedure(sp_name, params)

def ver_AreaID(ID):
    sp_name = "spVerAreasID"
    params = [ID]
    return execute_stored_procedure(sp_name, params)
    