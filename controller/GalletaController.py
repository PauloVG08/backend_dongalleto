from aifc import Error
from bd.Conexion import startConexion
from model.Galleta import Galleta

def getAllGalletas():
    conexion, cursor = startConexion()
    try:
        estatus = 1
        consulta = f"SELECT * FROM galleta WHERE estatus = {estatus}"
        cursor.execute(consulta)
        result = cursor.fetchall()

        galletas = []

        for galleta in result:
            response = dataToGalleta(galleta)
            galletas.append(response)

        cursor.close()
        conexion.close()
        return galletas
    except:
        cursor.close()
        conexion.close()
        return None

def insertarGalleta(galleta: Galleta):
    try:
        conexion, cursor = startConexion()

        query = "INSERT INTO galleta(nombre, descripcion, precio, cantidad, img, estatus)VALUES (%s, %s, %s, %s,%s, %s)"
        valores = (galleta.nombre, galleta.descripcion, galleta.precio, galleta.cantidad, galleta.img, galleta.estatus)
        cursor.execute(query, valores)
        conexion.commit()

        cursor.close()
        conexion.close()
        return True
    except Error as e:
        print("Error: ", e)
        cursor.close()
        conexion.close()
        return False

def actualizarGalleta(galleta: Galleta):
    try:
        conexion, cursor = startConexion()
        print("BD")
        print(galleta)

        query = "UPDATE galleta SET nombre = %s, descripcion = %s, precio = %s, cantidad = %s where idGalleta = %s"
        valores = (galleta.nombre, galleta.descripcion, galleta.precio, galleta.cantidad, galleta.idGalleta)
        cursor.execute(query, valores)

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
        consulta = f'UPDATE galleta SET estatus = {status}  WHERE idGalleta ={id}'

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

def dataToGalleta(data):
    return Galleta(
        idGalleta=data[0],
        nombre=data[1],
        descripcion=data[2],
        precio=data[3],
        cantidad=data[4],
        img=data[5],
        estatus=data[6]
    )
