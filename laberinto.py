from hierba import hierba
from roca import roca
from azucar import azucar
from vino import vino
from veneno import veneno

class laberinto:
    def __init__(self, canvas, width, height):
        self.matriz = [[hierba(canvas, 15 + 30*i, 15 + 30*j) for i in range(height)] for j in range(width)]