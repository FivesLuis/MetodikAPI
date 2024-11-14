from app.utils.db_helpers import execute_stored_procedure

def ver_preciosRutas():
    sp_name = "spVerPreciosRutas"
    params = []
    return execute_stored_procedure(sp_name, params)

def act_preciosRuta(data):
    sp_name = "spActPreciosRuta"
    params = [
        data.get("ID"), 
        data.get("PrecioAdulto"),
        data.get("PrecioInfantil"),
        data.get("PrecioInapam"),
        data.get("PrecioRedondo"),
    ]
    return execute_stored_procedure(sp_name, params)

def afectar_CambioPreciosRuta(data):
    sp_name = "spAfectarCambioPreciosRuta"
    params = [
        data.get("EmpresaID"), 
    ]
    return execute_stored_procedure(sp_name, params)