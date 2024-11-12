import random
import numpy as np
import matplotlib.pyplot as plt  # Importa Matplotlib para graficar
from tkinter import PhotoImage

class Hormiga:
    def __init__(self, canvas, x, y):
        # Atributos de la hormiga
        self.name = "hormiga"
        self.canvas = canvas
        self.posicion = np.array([[x], [y]])  # Posición inicial
        self.salud = 100
        self.nivel_alcohol = 0
        self.puntos = 0
        self.imagen = PhotoImage(file="imagenes/icons8-hormiga-30.png")
        self.id = self.canvas.create_image(x, y, image=self.imagen)
        self.historial_movimientos = []
        self.secuencia_movimientos = self.inicializar_movimiento()
        self.umbral_mejora = 5
        self.puntajes_generacionales = []  # Lista para almacenar los mejores puntajes por generación

    # Inicialización de secuencias de movimiento
    def inicializar_movimiento(self):
        secuencias_optimas = self.cargar_mejores_secuencias()
        if secuencias_optimas:
            return secuencias_optimas[0]
        return self.generar_secuencia_movimientos()

    # Método para mover la hormiga en el laberinto
    def mover(self, direccion, laberinto):
        movimientos = {
            "arriba": np.array([[0], [-1]]),
            "abajo": np.array([[0], [1]]),
            "izquierda": np.array([[-1], [0]]),
            "derecha": np.array([[1], [0]])
        }
        
        if direccion in movimientos:
            desplazamiento = movimientos[direccion]
            nueva_posicion = self.posicion + desplazamiento
            nueva_x, nueva_y = int(nueva_posicion[0][0]), int(nueva_posicion[1][0])
            
            if laberinto.es_posicion_valida(nueva_x, nueva_y):
                self.posicion = nueva_posicion
                self.canvas.move(self.id, desplazamiento[0][0] * 30, desplazamiento[1][0] * 30)
                self.historial_movimientos.append(direccion)
                item = laberinto.obtener_item(nueva_x, nueva_y)
                if item:
                    self.comer(item, laberinto, nueva_x, nueva_y)
                return True
        return False

    # Método para consumir un ítem
    def comer(self, item, laberinto, x, y):
        if item == "azúcar":
            self.puntos += 10
        elif item == "vino":
            self.nivel_alcohol += 5
            if self.nivel_alcohol > 50:
                self.salud -= 10
        elif item == "veneno":
            self.salud = 0
        laberinto.eliminar_item(x, y)

    # Generar secuencia de movimientos aleatoria
    def generar_secuencia_movimientos(self):
        return [random.choice(["arriba", "abajo", "izquierda", "derecha"]) for _ in range(10)]

    # Evaluar secuencia de movimientos
    def evaluar_secuencia(self, secuencia, laberinto):
        puntos = 0
        for movimiento in secuencia:
            if self.mover(movimiento, laberinto):
                puntos += 1
        return puntos

    # Guardar y cargar mejores secuencias, y el algoritmo genético adaptativo
    def guardar_mejores_secuencias(self, archivo="mejores_secuencias.txt"):
        with open(archivo, "w") as file:
            for movimiento in self.historial_movimientos:
                file.write(f"{movimiento}\n")
    
    def cargar_mejores_secuencias(self, archivo="mejores_secuencias.txt"):
        secuencias = []
        try:
            with open(archivo, "r") as file:
                secuencia_actual = []
                for line in file:
                    if line.strip():
                        secuencia_actual.append(line.strip())
                    else:
                        secuencias.append(secuencia_actual)
                        secuencia_actual = []
        except FileNotFoundError:
            pass
        return secuencias[:3]

    def algoritmo_genetico_adaptativo(self, generaciones, laberinto):
        poblacion = self.cargar_mejores_secuencias() + [self.generar_secuencia_movimientos() for _ in range(7)]
        for gen in range(generaciones):
            puntuaciones = [(self.evaluar_secuencia(sec, laberinto), sec) for sec in poblacion]
            puntuaciones.sort(reverse=True, key=lambda x: x[0])

            # Guardar el mejor puntaje de esta generación
            mejor_puntaje = puntuaciones[0][0]
            self.puntajes_generacionales.append(mejor_puntaje)  # Agrega el mejor puntaje de cada generación
           
            if puntuaciones[0][0] < self.umbral_mejora:
                nueva_poblacion = [self.mutar_secuencia(sec) for _, sec in puntuaciones]
            else:
                nueva_poblacion = [self.cruzar_secuencias(puntuaciones[0][1], puntuaciones[1][1])]
                nueva_poblacion += [self.mutar_secuencia(sec) for _, sec in puntuaciones[2:]]

            poblacion = nueva_poblacion

        self.historial_movimientos = puntuaciones[0][1]
        self.guardar_mejores_secuencias()

    def cruzar_secuencias(self, secuencia1, secuencia2):
        punto_cruce = random.randint(0, len(secuencia1) - 1)
        return secuencia1[:punto_cruce] + secuencia2[punto_cruce:]

    def mutar_secuencia(self, secuencia):
        secuencia[random.randint(0, len(secuencia) - 1)] = random.choice(["arriba", "abajo", "izquierda", "derecha"])
        return secuencia

    # Registrar estadísticas de generación y analizar progreso
    def registrar_estadisticas(self, generacion, archivo="estadisticas_simulacion.txt"):
        with open(archivo, "a") as file:
            file.write(f"Generación: {generacion}, Puntaje: {self.puntos}, Salud: {self.salud}, Movimientos: {self.historial_movimientos}\n")

    def analizar_estadisticas(self, archivo="estadisticas_simulacion.txt"):
        puntajes = []
        try:
            with open(archivo, "r") as file:
                for line in file:
                    if "Puntaje" in line:
                        puntaje = int(line.split(":")[1].strip().split(",")[0])
                        puntajes.append(puntaje)
            if len(puntajes) > 5 and sum(puntajes[-5:]) / 5 < max(puntajes) * 0.9:
                return True
        except FileNotFoundError:
            pass

    # Método para graficar los puntajes generacionales
    def graficar_puntajes(self):
        plt.plot(self.puntajes_generacionales, marker='o')
        plt.title("Evolución de los Puntajes en Generaciones")
        plt.xlabel("Generación")
        plt.ylabel("Puntaje")
        plt.show()

