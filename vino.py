from tkinter import PhotoImage
class vino:
    def __init__(self, canvas, x, y):
        self.name = "vino"
        self.alcohol = 10
        self.canvas = canvas
        self.x = x
        self.y = y
        self.imagen = PhotoImage(file="imagenes/icons8-copa-de-vino-30.png")
        self.id = self.canvas.create_image(self.x, self.y, image=self.imagen)
        self.box = self.canvas.bbox(self.id)