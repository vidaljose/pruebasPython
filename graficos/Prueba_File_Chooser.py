from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("150x50")
def abreFichero():
    fichero = filedialog.askopenfilename(title="Abrir", initialdir="/home", filetypes=(("Ficheros python", "*.py"), ("Ficheros de texto", "*.txt"), ("Todos los ficheros", "*.*")))
    print(fichero)

Button(root, text="Abrir fichero",command=abreFichero).pack()

root.mainloop()