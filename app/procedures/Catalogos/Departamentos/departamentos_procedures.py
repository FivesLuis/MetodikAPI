from app.utils.db_helpers import execute_stored_procedure

def ver_Departamentos(data):
    sp_name = "spVerDepartamentos"
    params = [
        data.get("PersonaID"),
        data.get("EmpresaID"),
        data.get("EstatusID"),
        data.get("FechaD"),
        data.get("FechaH")
    ]
    return execute_stored_procedure(sp_name, params)

def act_Departamento(data):
    sp_name = "spActDepartamento"
    params = [
        data.get("ID"),
        data.get("Nombre"),
        data.get("EstatusID"),
        data.get("PersonaID"),
        data.get("EmpresaID")
    ]
    return execute_stored_procedure(sp_name, params)

def ver_DepartamentoID(ID):
    sp_name = "spVerDepartamentoID"
    params = [ID]
    return execute_stored_procedure(sp_name, params)