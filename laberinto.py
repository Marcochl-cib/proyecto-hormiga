from hierba import hierba
from azucar import azucar
from vino import vino
from veneno import veneno
from roca import roca
from hormiga import hormiga


from hierba import Hierba
class Laberinto:
    def __init__(self, canvas, size):
        self.canvas = canvas
        self.size = size
        self.matriz = [[Hierba(self.canvas, 15 + 30 * i, 15 + 30 * j) for i in range(size)] for j in range(size)]

    def crear(self, num, x, y):
        """Crea un ítem en las coordenadas (x, y) y lo coloca en la matriz."""
        tipos_de_item = {
            0: Hierba,
            1: Azucar,
            2: Vino,
            3: Veneno,
            4: Roca
        }

        if num not in tipos_de_item:
            raise ValueError("Número de ítem no válido.")

        item_clase = tipos_de_item[num]
        item = item_clase(self.canvas, 15 + 30 * x, 15 + 30 * y, row=y, col=x)
        self.matriz[y][x] = item
        return item

    def eliminar_item(self, x, y):
        """Elimina el ítem en la posición (x, y) y lo reemplaza con hierba."""
        if 0 <= x < self.size and 0 <= y < self.size:
            item = self.matriz[y][x]
            # Elimina la imagen del ítem del Canvas
            self.canvas.delete(item.id)
            # Reemplaza el ítem eliminado con una instancia de Hierba
            self.matriz[y][x] = Hierba(self.canvas, 15 + 30 * x, 15 + 30 * y, row=y, col=x)


