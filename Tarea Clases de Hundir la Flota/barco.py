class Barco:
    def __init__(self, nombre, longitud):
        # Inicializamos los atributos obligatorios
        self.nombre = nombre
        self.longitud = longitud
        self.golpes_recibidos = 0  # Empieza siempre en 0

    def recibir_impacto(self):
        # Incrementamos el contador de golpes
        self.golpes_recibidos += 1

    def esta_hundido(self):
        # Devuelve True si los golpes igualan la longitud
        return self.golpes_recibidos == self.longitud

    def mostrar_estado(self):
        print(f"{self.nombre} | Golpes: {self.golpes_recibidos} | ¿Hundido?: {self.esta_hundido()}")

if __name__ == "__main__":
        # Bloque de pruebas

        # 1. Prueba con Submarino
        sub = Barco("Submarino", 1)
        sub.recibir_impacto()
        print(f"Submarino hundido: {sub.esta_hundido()}")

        # 2. Prueba con Buque
        buque = Barco("Buque", 3)

        buque.recibir_impacto()
        print(f"Buque hundido (1 golpe): {buque.esta_hundido()}")

        buque.recibir_impacto()
        buque.recibir_impacto()
        print(f"Buque hundido (3 golpes): {buque.esta_hundido()}")