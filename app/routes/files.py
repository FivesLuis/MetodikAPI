from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import os
from werkzeug.utils import secure_filename

# Crear el blueprint
files_bp = Blueprint('files', __name__)

# Carpeta base donde se guardarán todos los archivos
BASE_UPLOAD_FOLDER = './uploads'
if not os.path.exists(BASE_UPLOAD_FOLDER):
    os.makedirs(BASE_UPLOAD_FOLDER)

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
    relative_path = os.path.relpath(file_path, BASE_UPLOAD_FOLDER)
    return jsonify({
        "message": "Archivo subido con éxito",
        "path": relative_path,
        "Ok": "0"
    }), 200
