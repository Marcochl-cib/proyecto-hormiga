from hierba import hierba
from azucar import azucar
from vino import vino
from veneno import veneno
from roca import roca
from hormiga import hormiga


class laberinto:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.matriz = [[hierba(self.canvas, 15 + 30*i, 15 + 30*j) for i in range(height)] for j in range(width)]
    
    def crear(self, num, x, y):
        if num == 0:
            return hierba(self.canvas, x, y)
        elif num == 1:
            return azucar(self.canvas, x, y)
        elif num == 2:
            return vino(self.canvas, x, y)
        elif num == 3:
            return veneno(self.canvas, x, y)
        elif num == 4:
            return roca(self.canvas, x, y)
        elif num == 5:
            return hormiga(self.canvas, x, y)