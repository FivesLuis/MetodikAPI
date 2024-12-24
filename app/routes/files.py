from flask import Blueprint, request, jsonify, send_from_directory, send_file
from flask_jwt_extended import jwt_required
import os
from werkzeug.utils import secure_filename

# Crear el blueprint
files_bp = Blueprint('files', __name__)
filesView_bp = Blueprint('filesView', __name__)


BASE_URL = "http://127.0.0.1:5001"
# Carpeta base donde se guardarán todos los archivos
BASE_UPLOAD_FOLDER = os.path.abspath('uploads')
if not os.path.exists(BASE_UPLOAD_FOLDER):
    os.makedirs(BASE_UPLOAD_FOLDER)


@filesView_bp.route('/uploads/<path:filename>', methods=['GET'])
#@jwt_required()
def serve_file(filename):
    file_path = os.path.abspath(os.path.join(BASE_UPLOAD_FOLDER, filename))
    print(f"Ruta intentada: {file_path}")  # Debug
    if not os.path.exists(file_path):
        return jsonify({"error": "Archivo no encontrado", "ruta_intentada": file_path}), 404
    return send_file(file_path)

@files_bp.route('/Archivos/subirArchivo', methods=['POST'])
@jwt_required()
def subir_archivo():
    """
    Endpoint para subir archivos y organizarlos por tipo y extensión.
    """
    file = request.files.get('file')
    file_type = request.form.get('tipo')  # Parámetro 'tipo' para clasificar (Facturas, Reportes, etc.)

    if not file or not file_type:
        return jsonify({"error": "Faltan datos requeridos: archivo o tipo", "Ok": "1"}), 400

    # Asegurar nombre seguro y obtener extensión
    filename = secure_filename(file.filename)
    file_extension = filename.split('.')[-1].lower()

    # Crear carpetas dinámicamente según 'tipo' y extensión
    folder_path = os.path.join(BASE_UPLOAD_FOLDER, file_type, file_extension)
    os.makedirs(folder_path, exist_ok=True)

    # Guardar el archivo
    file_path = os.path.join(folder_path, filename)
    file.save(file_path)

    # Devolver la ruta relativa del archivo
    public_url = f"{BASE_URL}/uploads/{file_type}/{file_extension}/{filename}"
    return jsonify({
        "message": "Archivo subido con éxito",
        "path": public_url,
        "Ok": "0"
    }), 200

@files_bp.route('/Archivos/<path:filename>', methods=['GET'])
def descargar_archivo(filename):
    """
    Endpoint para servir un archivo previamente subido.
    La ruta accesible será: /Archivos/<ruta_relativa>
    Por ejemplo: /Archivos/Tickets/png/LogoNew.png
    """
    full_path = os.path.join(BASE_UPLOAD_FOLDER, filename)
    print("Intentando servir:", full_path)
    print("Existe el archivo?", os.path.isfile(full_path))

    # Si el archivo no existe, se retornará 404 automáticamente
    return send_from_directory(BASE_UPLOAD_FOLDER, filename)