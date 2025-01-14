from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)

# Habilitar CORS
CORS(app)

# Configuración de la base de datos
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",          # Cambia esto si tu base de datos no está en localhost
        user="root",
        password="12121212",
        database="kevin"
    )
    return connection

# Ruta de inicio
@app.route('/')
def home():
    return "¡Hola, mundo desde Flask!"

# Ejemplo de una API REST (GET) para obtener todos los registros de la tabla 'inventario'
@app.route('/api/inventario', methods=['GET'])
def get_inventario():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM inventario")
        inventario = cursor.fetchall()
    finally:
        cursor.close()
        connection.close()
    
    return jsonify(inventario)

@app.route('/api/inventario/<codigo>', methods=['GET'])
def get_inventario_by_codigo(codigo):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM inventario WHERE codigo = %s", (codigo,))
        inventario = cursor.fetchall()
        if not inventario:
            return jsonify({"mensaje": "No se encontraron resultados para el código especificado."}), 404
    finally:
        cursor.close()
        connection.close()
    
    return jsonify(inventario)


if __name__ == '__main__':
    app.run(debug=True)
