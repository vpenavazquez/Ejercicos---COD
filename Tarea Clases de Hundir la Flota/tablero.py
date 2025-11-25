class Tablero:
    def __init__(self, tamano):
        self.dimensiones = tamano
        # Crea una lista de listas llena de 0s (Agua)
        self.casillas = [[0] * tamano for _ in range(tamano)]

    def mostrar_tablero(self):
        # Imprime cada fila de la matriz
        for fila in self.casillas:
            print(fila)

if __name__ == "__main__":
        # Bloque de pruebas

        # Instancia tablero de 5x5
        tablero = Tablero(5)


        tablero.mostrar_tablero()