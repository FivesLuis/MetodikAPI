from app.procedures.Catalogos.Perfiles.perfiles_procedures import *

def verPerfiles(EstatusID, EmpresaID, Buscar):
    return ver_Perfiles(EstatusID, EmpresaID, Buscar)

def verPerfilID(ID):
    return ver_PerfilID(ID)

def actPerfil(data):
    return act_Perfil(data)

def verModulosAcceso(PerfilID, PersonaID):
    return ver_ModulosAcceso(PerfilID, PersonaID)

def actAccesosPerfil(data):
    return act_accesosPerfil(data)

def crearMenus(PersonaID):
    return crear_menus(PersonaID)

def actModuloFavorito(data):
    return actModulo_Favorito(data)

def verModulosFavoritos(PersonaID):
    return verModulos_Favoritos(PersonaID)