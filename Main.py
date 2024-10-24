from tkinter import Tk, Button, Label, Scale, Canvas, IntVar
import time
from laberinto import laberinto
from roca import roca

root = Tk()
root.geometry("500x500")

width_tablero = IntVar()
scale_width_tablero = Scale(from_=3, to=10, orient="horizontal", tickinterval=1, label="Ancho", command=width_tablero, showvalue=False)

height_tablero = IntVar()
scale_height_tablero = Scale(from_=3, to=10, orient="horizontal", tickinterval=1, label="Altura", command=height_tablero, showvalue=False)

scale_width_tablero.pack()
scale_height_tablero.pack()

canva = Canvas(root, width=5*30, height=10*30, bg="green")

hola = laberinto(canva, 5, 10)



hola.matriz[0][1] = roca(canva, 15+0*30, 15+1*30)
canva.pack()


root.mainloop()