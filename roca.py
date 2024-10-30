from tkinter import PhotoImage
class roca:
    def __init__(self, canvas, x, y):
        self.name = "roca"
        self.canvas = canvas
        self.x = x
        self.y = y
        self.imagen = PhotoImage(file="imagenes/icons8-roca-30.png")
        self.id = self.canvas.create_image(self.x, self.y, image=self.imagen)
        self.box = self.canvas.bbox(self.id)