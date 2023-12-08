from bd.Conexion import startConexion
from mysql.connector import Error

def getAllDetalleVenta(fecha):
    conexion, cursor = startConexion()
    try:
        consulta = f"SELECT * FROM VistaDetalleVentaPorFecha WHERE fecha = '{fecha}'"
        cursor.execute(consulta)
        result = cursor.fetchall()

        cursor.close()
        conexion.close()

        return result
    except:
        cursor.close()
        conexion.close()
        return None
