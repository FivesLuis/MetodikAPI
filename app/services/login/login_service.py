from app.procedures.login.login_procedures import login, verEmpresas_Usuario

def login_usuario(Correo, Contrasena, Empresa):
    """
    Llama al procedimiento almacenado de login y devuelve los resultados.
    """
    return login(Correo, Contrasena, Empresa)

def verEmpresasUsuario(PersonaID):
    """
    Llama al procedimiento almacenado de login y devuelve los resultados.
    """
    return verEmpresas_Usuario(PersonaID)
