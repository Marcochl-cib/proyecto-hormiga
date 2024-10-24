from tkinter import PhotoImage
class veneno:
    def __init__(self, canvas, x, y):
        self.name = "veneno"
        self.points = -10
        self.canvas = canvas
        self.x = x
        self.y = y
        self.imagen = PhotoImage(file="imagenes/icons8-botella-de-veneno-30.png")
        self.id = self.canvas.create_image(self.x, self.y, image=self.imagen)