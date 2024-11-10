from tkinter import Tk, Button, Label, Entry, Canvas, IntVar, Radiobutton
from laberintoM import Laberinto  # Asegúrate de que la clase Laberinto esté importada correctamente

root = Tk()
root.geometry("500x500")
fuente = ("Arial", 12)

canva = Canvas()
tablero = None
editable = False

def mostrar_inicio():
    label_size_tablero.pack()
    entry_size_tablero.pack()
    boton_crear.pack()

def ocultar_inicio():
    label_size_tablero.forget()
    entry_size_tablero.forget()
    boton_crear.forget()

def crear_tablero():
    global canva, tablero
    
    # Obtener el tamaño ingresado por el usuario
    try:
        size = int(entry_size_tablero.get())
        if not (3 <= size <= 10):
            raise ValueError("El tamaño debe estar entre 3 y 10.")
    except ValueError:
        print("Por favor, ingrese un tamaño válido entre 3 y 10.")
        return
    
    # Configurar el Canvas y el tablero
    canva = Canvas(root, width=size * 30, height=size * 30, bg="green")
    canva.pack(anchor="nw")  # Muestra el Canvas en la ventana
    tablero = Laberinto(canva, size)  # Crear el laberinto con el tamaño ingresado

def mostrar_edit():
    global editable
    editable = True
    for boton in [boton_hierba, boton_azucar, boton_vino, boton_veneno, boton_roca, boton_hormiga]:
        boton.pack(anchor="ne")

def editar(event):
    global tablero, obj, editable
    if not editable:
        return

    # Convertir coordenadas de clic a coordenadas de la matriz
    celda_x, celda_y = event.x // 30, event.y // 30

    # Verificar que las coordenadas estén dentro de los límites del tablero
    if 0 <= celda_x < tablero.size and 0 <= celda_y < tablero.size:
        tablero.eliminar_item(celda_x, celda_y)  # Eliminar ítem actual en la celda
        tablero.matriz[celda_y][celda_x] = tablero.crear(obj.get(), celda_x, celda_y)

canva.bind("<Button-1>", editar)

# Crear un Label y Entry para el tamaño del tablero
label_size_tablero = Label(root, text="Dimensiones (3 a 10):", font=fuente)
entry_size_tablero = Entry(root, font=fuente, width=5)

# Botón para crear el tablero
boton_crear = Button(text="Crear", font=fuente, command=lambda: [crear_tablero(), ocultar_inicio(), mostrar_edit()])

# Botones de opción para seleccionar el tipo de ítem
obj = IntVar(value=0)
boton_hierba = Radiobutton(text="Hierba", font=fuente, variable=obj, value=0)
boton_azucar = Radiobutton(text="Azúcar", font=fuente, variable=obj, value=1)
boton_vino = Radiobutton(text="Vino", font=fuente, variable=obj, value=2)
boton_veneno = Radiobutton(text="Veneno", font=fuente, variable=obj, value=3)
boton_roca = Radiobutton(text="Roca", font=fuente, variable=obj, value=4)
boton_hormiga = Radiobutton(text="Hormiga", font=fuente, variable=obj, value=5)

# Muestra el inicio
mostrar_inicio()
root.mainloop()
