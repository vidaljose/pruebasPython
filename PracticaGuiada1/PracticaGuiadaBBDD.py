from tkinter import *
from tkinter import messagebox
import sqlite3
#from PracticaGuiada1 import PracticaGuiada

def crearDB():
    try:
        miConexion = sqlite3.connect("PracticaGuiadaBBDD.db")
        miCursor =  miConexion.cursor()
        miCursor.execute('''
            CREATE TABLE PRODUCTOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            NOMBRE VARCHAR(50) UNIQUE,
            PASS VARCHAR(50),
            APELLIDO VARCHAR(50),
            DIRECCION VARCHAR(50),
            COMENTARIOS TEXT)
            ''')
        miConexion.commit()
        miConexion.close()
        messagebox.showinfo("MENSAJE", "La base de datos se creo exitosamente")
    except:
        messagebox.showwarning("ALERTA", "La base de datos ya existe")

def insertarDB(nombre,clave,apellido,direccion,comentarios):
    try:
        miConexion = sqlite3.connect("PracticaGuiadaBBDD.db")
        miCursor =  miConexion.cursor()
        elementos = (nombre,clave,apellido,direccion,comentarios)
        miCursor.execute(f"INSERT INTO PRODUCTOS VALUES (NULL,'{nombre}','{clave}','{apellido}','{direccion}','{comentarios}')")
        miConexion.commit()
        miConexion.close()
        messagebox.showinfo("MENSAJE", "Se inserto el dato con exito")
    except Exception as e:
        messagebox.showwarning("ERROR", e)

def leerDB(id):
    if isinstance(id,int):

        try:
            miConexion = sqlite3.connect("PracticaGuiadaBBDD.db")
            miCursor = miConexion.cursor()
            miCursor.execute(f"SELECT * FROM PRODUCTOS WHERE ID = '{id}'")
            producto = miCursor.fetchall()
            miConexion.commit()
            miConexion.close()

            return producto
        except Exception as e:
            messagebox.showwarning("ERROR", e)
            return 0
    else:
        messagebox.showwarning("ERROR","El id tiene que ser de tipo entero")

def actualizarDB(id,nombre,clave,apellido,direccion,comentarios):
    try:
        miConexion = sqlite3.connect("PracticaGuiadaBBDD.db")
        miCursor =  miConexion.cursor()
        miCursor.execute(f"UPDATE PRODUCTOS SET NOMBRE = '{nombre}',PASS = '{clave}',APELLIDO = '{apellido}',DIRECCION = '{direccion}',COMENTARIOS = '{comentarios}' WHERE ID = {id} ")
        miConexion.commit()
        miConexion.close()
        messagebox.showinfo("MENSAJE", "Se actualizo el dato con exito")
    except Exception as e:
        messagebox.showwarning("ERROR", e)

def borrarElementoDB(id):
    try:
        miConexion = sqlite3.connect("PracticaGuiadaBBDD.db")
        miCursor =  miConexion.cursor()
        seleccion = messagebox.askokcancel("BORRAR",f"Desea borrar el elemento id:{id}")
        if seleccion:
            miCursor.execute(f"DELETE FROM PRODUCTOS WHERE ID = {id}")
            #print(seleccion)
            miConexion.commit()
            miConexion.close()
            messagebox.showinfo("MENSAJE", f"Se borro el elemento id:{id}")
        else:
            messagebox.showinfo("MENSAJE", f"No se borro el elemento id:{id}")
        return seleccion
    except Exception as e:
        messagebox.showwarning("ERROR", e)