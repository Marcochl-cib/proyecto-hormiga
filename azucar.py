from tkinter import PhotoImage
class azucar:
    def __init__(self, canvas, x, y):
        self.name = "azucar"
        self.points = 10
        self.canvas = canvas
        self.x = x
        self.y = y
        self.imagen = PhotoImage(file="imagenes/icons8-azúcar-30.png")
        self.id = self.canvas.create_image(self.x, self.y, image=self.imagen)
    
    def consumir(self):
        self.canvas.delete(self.id)