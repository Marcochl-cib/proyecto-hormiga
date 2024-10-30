from tkinter import PhotoImage
class hormiga:
    def __init__(self, canvas, x, y):
        self.name = "hormiga"
        self.canvas = canvas
        self.x = x
        self.y = y
        self.imagen = PhotoImage(file="imagenes/icons8-hormiga-30.png")
        self.id = self.canvas.create_image(self.x, self.y, image=self.imagen)
        self.box = self.canvas.bbox(self.id)