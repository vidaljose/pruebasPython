from tkinter import *
from tkinter import messagebox

root = Tk()
def infoAdicional():
    messagebox.showinfo("Procesador de vidal", "Procesador de texto 2019")

def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salirAplicacion():
    #valor = messagebox.askquestion("Salir","Deseas salir de la aplicacion?")
    valor = messagebox.askokcancel("Salir", "Deseas salir de la aplicacion?")
    if valor==True:
        root.destroy()
def cerrarDocumento():
    valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar el documento")
    if valor == False:
        root.destroy()

#TODO: esto es una tarea
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu,tearoff=0)#agregar elementos al menu / tearoff elmina la linea del comienzo
archivoMenu.add_command(label="Nuevo")#agregar elementos al submenu
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar",command=cerrarDocumento)
archivoMenu.add_command(label="Salir",command =salirAplicacion)

archivoEdicion=Menu(barraMenu,tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu)

archivoAyuda=Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label="Licencia",command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de ..",command=infoAdicional)

barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
barraMenu.add_cascade(label="Edicion",menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas",menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)

root.mainloop()