class Tablero:
    def __init__(self, tamano):
        self.dimensiones = tamano
        # Crea una lista de listas llena de 0s (Agua)
        self.casillas = [[0] * tamano for _ in range(tamano)]

