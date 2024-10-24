from tkinter import PhotoImage
class hierba:
    def __init__(self, canvas, x, y):
        self.name = "hierba"
        self.canvas = canvas
        self.x = x
        self.y = y
        self.imagen = PhotoImage(file="imagenes/icons8-césped-30.png")
        self.id = self.canvas.create_image(self.x, self.y, image=self.imagen)