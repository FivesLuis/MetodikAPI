import pyodbc
from flask import jsonify
from app.utils.db import get_db_connection, close_db_connection

def verRutas():
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC spVerRutas")
        
        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return jsonify({"error": "No data returned from the procedure."}), 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return jsonify(results)
    except pyodbc.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            close_db_connection(conn)

def verRutasResumen(ID):
    conn = None 
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC spVerRutasResumen ?", ID)
        
        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return jsonify({"error": "No data returned from the procedure."}), 500
        
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return jsonify(results)
    except pyodbc.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            close_db_connection(conn)
        
def actRutas(data):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  # Asegúrate de que las transacciones se confirmen automáticamente
        
        query = "EXEC spActRuta ?,?,?,?,? ,?,?,?,?,? ,?,?,? "
        cursor.execute(query, data.get('ID'),data.get('Ruta'),data.get('Zona'),data.get('Kms'),data.get('Costo'),data.get('SucursalD'),data.get('DestinoDID'),
                data.get('DestinoAID'),data.get('Observaciones'),data.get('EstatusID'),data.get('Tiempo'),data.get('UltimoCambio'), data.get('FechaRegistro'))
        
        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return jsonify({"error": "No data returned from the procedure."}), 500
        
        columns = [column[0] for column in cursor.description]
        
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return results, 200
    
    except pyodbc.Error as e:

        return jsonify({"error": str(e)}), 500
    
    finally:
        if conn:
            close_db_connection(conn)
