from app.utils.db_helpers import execute_stored_procedure


def ver_Conceptos(data):
    sp_name = "spVerConceptos"
    params = [
        data.get("PersonaID"),
        data.get("EmpresaID"),
        data.get("EstatusID"),
        data.get("FechaD"),
        data.get("FechaH")
    ]
    return execute_stored_procedure(sp_name, params)

def act_Concepto(data):
    sp_name = "spActConcepto"
    params = [
        data.get("ID"),
        data.get("ModuloID"),
        data.get("Concepto"),
        data.get("EstatusID"),
        data.get("Descripcion"),
        data.get("PersonaID"),
        data.get("EmpresaID")
    ]
    return execute_stored_procedure(sp_name, params)

def ver_ConceptoID(ID):
    sp_name = "spVerConceptoID"
    params = [ID]
    return execute_stored_procedure(sp_name, params)