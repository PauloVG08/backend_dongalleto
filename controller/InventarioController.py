from bd.Conexion import startConexion

def getAllInventarios():
    conexion, cursor = startConexion()
    try:
        consulta = f"SELECT * FROM inventario"
        cursor.execute(consulta)
        result = cursor.fetchall()

        cursor.close()
        conexion.close()

        return result
    except:
        cursor.close()
        conexion.close()
        return None

def insertarInventario(cantidad, nombre, caducidad, estatus):
    try:
        conexion, cursor = startConexion()
        
        args = (cantidad, nombre, caducidad, estatus)
        cursor.callproc("dongalleto.insertarInventario", args)

        conexion.commit()

        cursor.close()
        conexion.close()
        return True
    except:
        cursor.close()
        conexion.close()
        print("Algo salio mal en insert galleta")
        return False

def actualizarInventario(id, cantidad, nombre, caducidad, estatus):
    try:
        conexion, cursor = startConexion()

        args = (id, cantidad, nombre, caducidad, estatus)
        cursor.callproc("dongalleto.actualizarInventario", args)

        conexion.commit()

        cursor.close()
        conexion.close()
        return True
    except:
        cursor.close()
        conexion.close()
        print("Algo salio mal")
        return False

def eliminarInventario(id:int):
    try:
        conexion, cursor = startConexion()

        status = 0
        consulta = f'UPDATE inventario SET status = {status}  WHERE id ={id}'

        cursor.execute(consulta)

        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except:
        cursor.close()
        conexion.close()
        print("Algo salio mal")
        return False
