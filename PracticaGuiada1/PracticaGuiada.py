from tkinter import *
from tkinter import messagebox
from PracticaGuiada1 import PracticaGuiadaBBDD

raiz = Tk()
raiz.title("Practica Guiada")
# -------------------------------Variables
miId = IntVar()
miNombre = StringVar()
miPass = StringVar()
miApellido = StringVar()
miDireccion = StringVar()
miComentario = StringVar()
# -------------------------------Algunas funciones

def borrarFormulario():
    miId.set("")
    miNombre.set("")
    miPass.set("")
    miApellido.set("")
    miDireccion.set("")
    textoComentario.delete('1.0', END)
    #miComentario.set("")

def insertarYBorrar():
    PracticaGuiadaBBDD.insertarDB(miNombre.get(), miPass.get(), miApellido.get(), miDireccion.get(), textoComentario.get('1.0', END))
    borrarFormulario()

def leerProductos(id):
    borrarFormulario()
    try:
        elemento =  PracticaGuiadaBBDD.leerDB(id)
        #print(elemento[0][1])
        miId.set(elemento[0][0])
        miNombre.set(elemento[0][1])
        miPass.set(elemento[0][2])
        miApellido.set(elemento[0][3])
        miDireccion.set(elemento[0][4])
        textoComentario.insert(INSERT,elemento[0][5])
    except:
        messagebox.showwarning("ERROR","El elemento no se encuentra en la base de datos")
        borrarFormulario()

def actualizarYBorrar():
    PracticaGuiadaBBDD.actualizarDB(miId.get(),miNombre.get(), miPass.get(), miApellido.get(), miDireccion.get(), textoComentario.get('1.0', END))
    borrarFormulario()

def borrarDeDB():
    if PracticaGuiadaBBDD.borrarElementoDB(miId.get()):
        borrarFormulario()
def infoAdicional():
    messagebox.showinfo("vidal", "Practica Guiada 1.0")

def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")
# -------------------------------Menu
barraMenu = Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu,tearoff=0)#agregar elementos al menu / tearoff elmina la linea del comienzo
archivoMenu.add_command(label="Conectar",command = PracticaGuiadaBBDD.crearDB)#agregar elementos al submenu
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command = raiz.destroy)


archivoBorrar=Menu(barraMenu,tearoff=0)
archivoBorrar.add_command(label="Borrar Formulario",command = borrarFormulario)

archivoCrud=Menu(barraMenu,tearoff = 0)
archivoCrud.add_command(label="Insertar", command = insertarYBorrar)
archivoCrud.add_command(label="Leer", command = lambda: leerProductos(miId.get()))
archivoCrud.add_command(label="Actualizar", command = actualizarYBorrar)
archivoCrud.add_command(label="Borrar", command = borrarDeDB)

archivoAyuda=Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label="Licencia", command = avisoLicencia)
archivoAyuda.add_command(label="Acerca de ..", command = infoAdicional)

barraMenu.add_cascade(label="BBDD",menu=archivoMenu)
barraMenu.add_cascade(label="Borrar",menu=archivoBorrar)
barraMenu.add_cascade(label="CRUD",menu=archivoCrud)
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)


# -------------------------------Formulario

miFrame1 = Frame(raiz,width=1200,height=600)
miFrame1.pack()


miId.set("")
cuadroId = Entry(miFrame1,textvariable=miId)
cuadroId.grid(row=0,column=1)
cuadroId.config(fg="blue",justify="center")

cuadroNombre = Entry(miFrame1,textvariable=miNombre)
cuadroNombre.grid(row=1,column=1)
cuadroNombre.config(fg="red",justify="center")

cuadroPass = Entry(miFrame1, textvariable = miPass)
cuadroPass.grid(row=2,column=1)
cuadroPass.config(show="?")

cuadroApellido = Entry(miFrame1, textvariable = miApellido)
cuadroApellido.grid(row=3,column=1)

cuadroDireccion = Entry(miFrame1, textvariable = miDireccion)
cuadroDireccion.grid(row=4,column=1)

textoComentario = Text(miFrame1,width=16,height=5) #tamano del cuadro de texto
textoComentario.grid(row=5,column=1,padx=10,pady=10)

scrollVert = Scrollbar(miFrame1,command=textoComentario.yview)
scrollVert.grid(row=5,column=2,sticky="nsew") #stiky="nsew adapta el tamano"/
textoComentario.config(yscrollcommand=scrollVert.set)#agrega el scroll para que se conecte en todo momento con el texto

IdLabel = Label(miFrame1,text="ID:")
IdLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

nombreLabel = Label(miFrame1,text="Nombre:")
nombreLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

passLabel = Label(miFrame1,text="Pass:")
passLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

apellidoLabel = Label(miFrame1,text="Apellido:")
apellidoLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

direccionLabel = Label(miFrame1,text="Direccion:")
direccionLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

comentariosLabel = Label(miFrame1,text="Comentarios:")
comentariosLabel.grid(row=5,column=0,sticky="e",padx=10,pady=10)


"""def codigoBoton():
    miNombre.set("Vidal")

botonEnvio=Button(raiz,text="Enviar",command=codigoBoton)
botonEnvio.pack()"""

# -----------------------------------------------------Botones

miFrame2 = Frame(raiz,width=1200,height=50)
miFrame2.pack()

botonInsertar = Button(miFrame2,text = "Insert",command = insertarYBorrar)
botonRead = Button(miFrame2,text = "Read",command = lambda: leerProductos(miId.get()))
botonUpdate = Button(miFrame2,text = "Update",command = actualizarYBorrar)
botonDelete = Button(miFrame2,text = "Delete", command = borrarDeDB)

botonInsertar.grid(row=0,column=0,padx=1,pady=2)
botonRead.grid(row=0,column=1,padx=1,pady=2)
botonUpdate.grid(row=0,column=2,padx=1,pady=2)
botonDelete.grid(row=0,column=3,padx=1,pady=2)

# ---------------------------------------------

raiz.mainloop()
