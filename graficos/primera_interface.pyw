from tkinter import *
#hay que colocar la w despues de py para que no salga el terminal
raiz = Tk()
raiz.title("Ventana de pruebas")
#raiz.resizable(True,True)#evita que se modifique el tamano
raiz.iconbitmap("gato.ico")
#raiz.geometry("650x350")
raiz.config(bg = "blue")
raiz.config(bd=45)
raiz.config(relief="groove")
#miFrame.config(cursor="hand2")
raiz.config(cursor="hand2")

miFrame = Frame() #frame
miFrame.pack()#colocando el frame en la raiz fill = "both" , expand="True" para llenarlo todo
miFrame.config(bg="red")
miFrame.config(width="650",height="350")
miFrame.config(bd=35)
miFrame.config(relief="sunken")
#miFrame.config(cursor="hand2")
miFrame.config(cursor="pirate")

raiz.mainloop()
