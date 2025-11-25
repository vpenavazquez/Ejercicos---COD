class Barco:
    def __init__(self, nombre, longitud):
        # Inicializamos los atributos obligatorios
        self.nombre = nombre
        self.longitud = longitud
        self.golpes_recibidos = 0  # Empieza siempre en 0

    def recibir_impacto(self):
        # Incrementamos el contador de golpes
        self.golpes_recibidos += 1