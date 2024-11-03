from hierba import hierba
from azucar import azucar
from vino import vino
from veneno import veneno
from roca import roca
from hormiga import hormiga
class Laberinto:
    # Define límites de tamaño de la matriz cuadrada
    MIN_SIZE = 3
    MAX_SIZE = 10

    def __init__(self, canvas, size):
        if not (self.MIN_SIZE <= size <= self.MAX_SIZE):
            raise ValueError(f"El tamaño del laberinto debe estar entre {self.MIN_SIZE}x{self.MIN_SIZE} y {self.MAX_SIZE}x{self.MAX_SIZE}.")
        
        self.canvas = canvas
        self.size = size
        # Inicializa la matriz cuadrada con objetos 'hierba' en cada celda
        self.matriz = [[hierba(self.canvas, 15 + 30 * i, 15 + 30 * j) for i in range(size)] for j in range(size)]
    
    def crear(self, num, x, y):
        """Crea un ítem en las coordenadas especificadas y lo coloca en la matriz."""
        if not (0 <= x < self.size and 0 <= y < self.size):
            raise IndexError("Coordenadas fuera de los límites del laberinto.")
        
        tipos_de_item = {
            0: hierba,
            1: azucar,
            2: vino,
            3: veneno,
            4: roca,
            5: hormiga
        }

        if num not in tipos_de_item:
            raise ValueError("Número de ítem no válido.")

        item_clase = tipos_de_item[num]
        item = item_clase(self.canvas, x, y)
        self.matriz[y][x] = item
        return item
    
    def obtener_item(self, x, y):
        """Obtiene el ítem en las coordenadas especificadas, si está dentro de los límites."""
        if 0 <= x < self.size and 0 <= y < self.size:
            return self.matriz[y][x]
        return None

    def eliminar_item(self, x, y):
        """Elimina el ítem en la posición especificada reemplazándolo por hierba."""
        if 0 <= x < self.size and 0 <= y < self.size:
            # Reemplaza el ítem por hierba en la posición (x, y)
            self.matriz[y][x] = hierba(self.canvas, x, y)
