from tkinter import *

raiz = Tk()
raiz.title("Calculadora")
miFrame = Frame(raiz)
miFrame.pack()
operacion = ""
resultado = 0

# -----------pantalla
numeroPantalla = StringVar()

pantalla = Entry(miFrame,textvariable = numeroPantalla)
pantalla.grid(row = 0, column=1,padx=10,pady=10,columnspan=4)
pantalla.config(background="black",fg= "#01DF74",justify = "right")
# -----------pulsaciones teclado
def numeroPulsado(num):
    global operacion
    if operacion !="":
        numeroPantalla.set(num)
        operacion=""
    else:
        numeroPantalla.set(numeroPantalla.get()+num)
def borrar():
    numeroPantalla.set("")
def suma(num):
    global operacion
    global resultado
    resultado+=int(num)
    operacion = "suma"
    numeroPantalla.set(resultado)

def restar():
    pass
def multiplicar():
    pass
def dividir():
    pass
def el_resultado():
    global resultado
    numeroPantalla.set(resultado+int(numeroPantalla.get()))
    resultado=0
#-----------botones CA BORRAR PANTALLA

boton7 =Button(miFrame,text="CA",width=18,command=borrar)
boton7.grid(row=1,column=1,columnspan=4)
#-----------fila 1
boton7 =Button(miFrame,text="7",width=3,command=lambda:numeroPulsado("7"))
boton8 =Button(miFrame,text="8",width=3,command=lambda:numeroPulsado("8"))
boton9 =Button(miFrame,text="9",width=3,command=lambda:numeroPulsado("9"))
botonDiv =Button(miFrame,text="/",width=3)

boton7.grid(row=2,column=1)
boton8.grid(row=2,column=2)
boton9.grid(row=2,column=3)
botonDiv.grid(row=2,column=4)

#-----------fila 2
boton4 =Button(miFrame,text="4",width=3,command=lambda:numeroPulsado("4")) #parentesis lo ejecuta de una vez
boton5 =Button(miFrame,text="5",width=3,command=lambda:numeroPulsado("5"))
boton6 =Button(miFrame,text="6",width=3,command=lambda:numeroPulsado("6"))
botonMult =Button(miFrame,text="X",width=3)

boton4.grid(row=3,column=1)
boton5.grid(row=3,column=2)
boton6.grid(row=3,column=3)
botonMult.grid(row=3,column=4)

#-----------fila 3
boton1 =Button(miFrame,text="1",width=3,command=lambda:numeroPulsado("1"))
boton2 =Button(miFrame,text="2",width=3,command=lambda:numeroPulsado("2"))
boton3 =Button(miFrame,text="3",width=3,command=lambda:numeroPulsado("3"))
botonRest =Button(miFrame,text="-",width=3)

boton1.grid(row=4,column=1)
boton2.grid(row=4,column=2)
boton3.grid(row=4,column=3)
botonRest.grid(row=4,column=4)

#-----------fila 4
boton0 =Button(miFrame,text="0",width=3,command=lambda:numeroPulsado("0"))
botonComa =Button(miFrame,text=",",width=3,command=lambda:numeroPulsado(","))
botonIgual =Button(miFrame,text="=",width=3,command=lambda:el_resultado())
botonSuma =Button(miFrame,text="+",width=3,command=lambda:suma(pantalla.get()))

boton0.grid(row=5,column=1)
botonComa.grid(row=5,column=2)
botonIgual.grid(row=5,column=3)
botonSuma.grid(row=5,column=4)


raiz.mainloop()
