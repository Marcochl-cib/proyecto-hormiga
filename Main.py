from tkinter import Tk, Button, Label, Scale, Canvas, IntVar, Radiobutton
import time
from laberinto import laberinto

root = Tk()
root.geometry("500x500")
fuente = ("Arial", 12)


canva = Canvas()
tablero = None

editable = False

def mostrar_inicio():
    scale_size_tablero.pack()
    boton_crear.pack()


def ocultar_inicio():
    scale_size_tablero.forget()
    boton_crear.forget()


def crear_tablero():
    global canva
    global tablero
    canva = Canvas(root, width=size_tablero.get()*30, height=size_tablero.get()*30, bg="green")
    tablero = laberinto(canva, size_tablero.get(), size_tablero.get())


def mostrar_edit():
    global editable
    editable = True
    canva.pack(anchor="nw")
    boton_hierba.pack(anchor="ne")
    boton_azucar.pack(anchor="ne")
    boton_vino.pack(anchor="ne")
    boton_veneno.pack(anchor="ne")
    boton_roca.pack(anchor="ne")

def editar(event):
    global tablero
    global obj
    print(event.x, event.y)
    if obj.get() is not None:
        for i in range(len(tablero.matriz)):
            for j in range(len(tablero.matriz[0])):
                x1, y1, x2, y2 = tablero.matriz[i][j].box()
                if  (x1 < event.x < x2) and (y1 < event.y < y2):
                    x, y = tablero.matriz[i][j].x, tablero.matriz[i][j].y
                    tablero.canvas.delete(tablero.matriz[i][j].id)
                    tablero.matriz[i][j] = tablero.crear(obj.get(), x, y)
                    print("me activo")
                    return

canva.bind("<Button-1>", editar)

size_tablero = IntVar()
scale_size_tablero = Scale(from_=3, to=10, orient="horizontal", tickinterval=1, label="Dimensiones", font=fuente, variable=size_tablero, showvalue=False)
boton_crear = Button(text="crear", font=fuente, command=lambda: [crear_tablero(), ocultar_inicio(), mostrar_edit()])

obj = IntVar(value=0)
boton_hierba = Radiobutton(text="Hierba", font=fuente, variable=obj, value=0)
boton_azucar = Radiobutton(text="Azucar", font=fuente, variable=obj, value=1)
boton_vino = Radiobutton(text="Vino", font=fuente, variable=obj, value=2)
boton_veneno = Radiobutton(text="Veneno", font=fuente, variable=obj, value=3)
boton_roca = Radiobutton(text="Roca", font=fuente, variable=obj, value=4)
boton_hormiga = Radiobutton(text="Hormiga", font=fuente, variable=obj, value=5)

mostrar_inicio()
root.mainloop()