from bd.Conexion import startConexion
from model.Galleta import Galleta

def getAllGalletas():
    conexion, cursor = startConexion()
    try:
        consulta = f"SELECT * FROM galleta"
        cursor.execute(consulta)
        result = cursor.fetchall()

        cursor.close()
        conexion.close()

        return result
    except:
        cursor.close()
        conexion.close()
        return None

def insertarGalleta(galleta: Galleta):
    try:
        conexion, cursor = startConexion()
        
        args = (galleta.nombre, galleta.descripcion, galleta.precio, galleta.cantidad, galleta.img, galleta.estatus)
        cursor.callproc("dongalleto.insertarGalletaV2", args)

        conexion.commit()

        cursor.close()
        conexion.close()
        return True
    except:
        cursor.close()
        conexion.close()
        print("Algo salio mal en insert galleta")
        return False

def actualizarGalleta(galleta: Galleta):
    try:
        conexion, cursor = startConexion()

        args = (galleta.id, galleta.nombre, galleta.descripcion, galleta.precio, galleta.cantidad, 
                galleta.img, galleta.estatus)
        cursor.callproc("dongalleto.actualizarGalleta", args)

        conexion.commit()

        cursor.close()
        conexion.close()
        return True
    except:
        cursor.close()
        conexion.close()
        print("Algo salio mal")
        return False

def eliminarGalleta(id:int):
    try:
        conexion, cursor = startConexion()

        status = 0
        consulta = f'UPDATE galleta SET status = {status}  WHERE id ={id}'

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

