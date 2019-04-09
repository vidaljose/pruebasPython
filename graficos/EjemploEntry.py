from tkinter import *

raiz = Tk()
miFrame = Frame(raiz,width=1200,height=600)
miFrame.pack()

miNombre=StringVar()

cuadroNombre = Entry(miFrame,textvariable=miNombre)
cuadroNombre.grid(row=0,column=1)
cuadroNombre.config(fg="red",justify="center")
cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1,column=1)
cuadroPass.config(show="?")
cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2,column=1)
cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3,column=1)
textoComentario = Text(miFrame,width=16,height=5) #tamano del cuadro de texto
textoComentario.grid(row=4,column=1,padx=10,pady=10)
scrollVert = Scrollbar(miFrame,command=textoComentario.yview)
scrollVert.grid(row=4,column=2,sticky="nsew") #stiky="nsew adapta el tamano"/
textoComentario.config(yscrollcommand=scrollVert.set)#agrega el scroll para que se conecte en todo momento con el texto

nombreLabel = Label(miFrame,text="Nombre:")
nombreLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)
passLabel = Label(miFrame,text="Pass:")
passLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)
apellidoLabel = Label(miFrame,text="Apellido:")
apellidoLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)
direccionLabel = Label(miFrame,text="Direccion:")
direccionLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)
comentariosLabel = Label(miFrame,text="Comentarios:")
comentariosLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

def codigoBoton():
    miNombre.set("Vidal")

botonEnvio=Button(raiz,text="Enviar",command=codigoBoton)
botonEnvio.pack()

raiz.mainloop()
