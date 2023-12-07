from bd.Conexion import startConexion
from mysql.connector import Error

def generar_venta(detallevp):
    r = False
    try:
        # Conectar a la base de datos
        conexion, cursor = startConexion()
        if conexion.is_connected():
            conexion.autocommit = False

            # Insertar en la tabla venta
            query1 = "INSERT INTO venta (fecha, total) VALUES (%s, %s)"
            cursor.execute(query1, (detallevp.venta.fecha, detallevp.venta.total))
            
            # Obtener el último ID insertado
            cursor.execute("SELECT LAST_INSERT_ID()")
            id_venta = cursor.fetchone()[0]
            detallevp.venta.id_venta = id_venta
            
            # Insertar en Detalle_Venta
            for item in detallevp.lista_galleta:
                query3 = "INSERT INTO Detalle_Venta (idVenta, idGalleta, cantidad, subtotal) VALUES (%s, %s, %s, %s)"
                cursor.execute(query3, (detallevp.venta.id_venta, item.galleta.id_galleta, item.galleta.cantidad, item.subtotal))
            
            conexion.commit()
            r = True
    except Error as e:
        print("Error: ", e)
        conexion.rollback()
        r = False
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
    return r

def getAllDetalleVenta(filtro):
    conexion, cursor = startConexion()
    try:
        consulta = f"SELECT * FROM venta WHERE fecha = {filtro}"
        cursor.execute(consulta)
        result = cursor.fetchall()

        cursor.close()
        conexion.close()

        return result
    except:
        cursor.close()
        conexion.close()
        return None
