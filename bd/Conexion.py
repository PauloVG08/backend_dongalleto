import mysql.connector

def startConexion():
    # Conectarse a la base de datos
    conexion = mysql.connector.connect(user='root', password='root',
                                       host='127.0.0.1', port=3306,
                                       database='donGalleto')
    if conexion.is_connected():
        cursor = conexion.cursor()
        return conexion, cursor
    else:
        print("Error: No se pudo conectar a la base de datos.")
