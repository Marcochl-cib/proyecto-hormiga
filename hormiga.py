import random
from tkinter import PhotoImage

class Hormiga:
    def __init__(self, canvas, x, y):
        # Atributos de la hormiga
        self.name = "hormiga"
        self.canvas = canvas
        self.x = x
        self.y = y
        self.posicion = (x, y)
        self.salud = 100
        self.nivel_alcohol = 0
        self.puntos = 0
        self.imagen = PhotoImage(file="imagenes/icons8-hormiga-30.png")
        self.id = self.canvas.create_image(self.x, self.y, image=self.imagen)
        self.historial_movimientos = []
        self.secuencia_movimientos = self.inicializar_movimiento()
        self.umbral_mejora = 5  # Umbral para la adaptación de mutación

    # Método para inicializar los movimientos basados en secuencias guardadas
    def inicializar_movimiento(self):
        secuencias_optimas = self.cargar_mejores_secuencias()
        if secuencias_optimas:
            return secuencias_optimas[0]  # Usa la mejor secuencia inicial
        return self.generar_secuencia_movimientos()

    # Método para mover la hormiga en el laberinto
    def mover(self, direccion, laberinto):
        movimientos = {
            "arriba": (0, -1),
            "abajo": (0, 1),
            "izquierda": (-1, 0),
            "derecha": (1, 0)
            }
        if direccion in movimientos:
            dx, dy = movimientos[direccion]
            nueva_x, nueva_y = self.x + dx, self.y + dy
            if laberinto.es_posicion_valida(nueva_x, nueva_y):
                self.x, self.y = nueva_x, nueva_y
                self.canvas.move(self.id, dx * 30, dy * 30)
                self.historial_movimientos.append(direccion)
                item = laberinto.obtener_item(self.x, self.y)
                if item:
                    self.comer(item, laberinto, self.x, self.y)  # Pasa laberinto y coordenadas a comer
            return True
        return False




    # Método para que la hormiga consuma un ítem
        def comer(self, item, laberinto, x, y):
            """La hormiga consume un ítem en su posición actual y el ítem se elimina."""
            if item == "azúcar":
                self.puntos += 10
            elif item == "vino":
                self.nivel_alcohol += 5
                if self.nivel_alcohol > 50:
                self.salud -= 10
            elif item == "veneno":
                self.salud = 0
            # Llama a eliminar_item en el laberinto para quitar el ítem de la posición actual
            laberinto.eliminar_item(x, y)  # La hormiga muere al consumir veneno

    # Generar una secuencia aleatoria de movimientos
    def generar_secuencia_movimientos(self):
        return [random.choice(["arriba", "abajo", "izquierda", "derecha"]) for _ in range(10)]

    # Evaluar una secuencia de movimientos
    def evaluar_secuencia(self, secuencia, laberinto):
        puntos = 0
        for movimiento in secuencia:
            if self.mover(movimiento, laberinto):
                puntos += 1  # Incrementar puntaje por cada movimiento válido
        return puntos

    # Guardar y cargar las mejores secuencias de movimientos
    def guardar_mejores_secuencias(self, archivo="mejores_secuencias.txt", n=10):
        # Cambia `n` al número de secuencias que deseas guardar
        with open(archivo, "w") as file:
            for movimiento in self.historial_movimientos[:n]:  # Limitar a las `n` mejores
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
            pass  # Si el archivo no existe, simplemente retorna una lista vacía
        return secuencias[:10]  # Retornar solo las 10 mejores secuencias

    # Método para mejorar el algoritmo genético adaptativo
    def algoritmo_genetico_adaptativo(self, generaciones, laberinto):
        poblacion = self.cargar_mejores_secuencias() + [self.generar_secuencia_movimientos() for _ in range(7)]
        for gen in range(generaciones):
            puntuaciones = [(self.evaluar_secuencia(sec, laberinto), sec) for sec in poblacion]
            puntuaciones.sort(reverse=True, key=lambda x: x[0])

            # Adaptar mutación según mejora
            if puntuaciones[0][0] < self.umbral_mejora:
                nueva_poblacion = [self.mutar_secuencia(sec) for _, sec in puntuaciones]
            else:
                nueva_poblacion = [self.cruzar_secuencias(puntuaciones[0][1], puntuaciones[1][1])]
                nueva_poblacion += [self.mutar_secuencia(sec) for _, sec in puntuaciones[2:]]

            poblacion = nueva_poblacion

        # Guardar la mejor secuencia y puntaje de la generación
        self.historial_movimientos = puntuaciones[0][1]
        self.guardar_mejores_secuencias()

    # Cruzar y mutar secuencias de movimiento
    def cruzar_secuencias(self, secuencia1, secuencia2):
        punto_cruce = random.randint(0, len(secuencia1) - 1)
        return secuencia1[:punto_cruce] + secuencia2[punto_cruce:]

    def mutar_secuencia(self, secuencia):
        secuencia[random.randint(0, len(secuencia) - 1)] = random.choice(["arriba", "abajo", "izquierda", "derecha"])
        return secuencia

    # Registrar y analizar las estadísticas
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
                return True  # Aumentar mutación si la mejora ha sido lenta
        except FileNotFoundError:
            pass
