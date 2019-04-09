from tkinter import *

root = Tk()
root.title("Programa de estudio")
miFrame = Frame(root,width = 800,height=800)
miFrame.pack()
miImagen = PhotoImage(file = "nerd.png")
miLabel=Label(miFrame,image = miImagen,fg = "red",font=("Comic Sans MS",18)).place(x=100,y=200)



root.mainloop()
