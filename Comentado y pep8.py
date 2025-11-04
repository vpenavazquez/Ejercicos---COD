#ahorcado jojos

import random  # Importa el módulo random para seleccionar palabras al azar

# Lista de frases relacionadas con personajes y stands del universo JoJo's
lista_palabras = [
    "jotaro kujo", "star platinum", "dio brando", "the world", "joseph joestar",
    "hermit purple", "josuke higashikata", "crazy diamond", "okuyasu nijimura",
    "the hand", "koichi hirose", "echoes", "rohan kishibe", "heaven’s door",
    "giorno giovanna", "gold experience", "bruno bucciarati", "sticky fingers",
    "narancia ghirga", "aerosmith", "guido mista", "sex pistols", "leone abbacchio",
    "moody blues", "trish una", "spice girl", "jolyne cujoh", "stone free",
    "enrico pucci", "made in heaven", "weather report", "foo fighters",
    "johnny joestar", "tusk", "gyro zeppeli", "yoshikage kira", "killer queen",
    "caesar zeppeli", "lisa lisa", "hol horse", "lucy steel", "hot pants",
    "diego brando", "scary monsters", "sandman", "in a silent way", "pocoloco",
    "hey ya!", "valentine", "dirty deeds done dirt cheap", "mountain tim",
    "oh! lonesome me", "josuke higashikata (jojolion)", "soft & wet",
    "yasuho hirose", "paisley park", "jobin higashikata", "speed king",
    "tooru", "wonder of u", "norisuke higashikata iv", "king nothing",
    "rai muromuzé", "born this way"
]

# Selecciona una palabra/frase aleatoria de la lista
palabra_secreta = random.choice(lista_palabras)

# Crea una lista con guiones bajos para ocultar las letras dejando los espacios visibles
letras_reveladas = [letra if letra == " " else "_" for letra in palabra_secreta]

# Número de intentos que tiene el jugador
numero_intentos = 10

print("Estás jugando al ahorcado de JoJo's")  # Mensaje de bienvenida

# Bucle principal del juego
while numero_intentos > 0:
    # Muestra el estado actual de la palabra con letras adivinadas
    print("Palabra:", " ".join(letras_reveladas))

    # Verifica si el jugador ha adivinado toda la palabra
    if "".join(letras_reveladas) == palabra_secreta:
        print("¡Buena! Adivinaste de una:", palabra_secreta)
        break  # Termina el juego si se adivinó correctamente

    # Solicita al jugador que ingrese una letra
    letra_ingresada = input("Adivina una letra: ").lower()

    # Verifica si la letra está en la palabra secreta
    if letra_ingresada in palabra_secreta:
        print("¡Lesgoo, bien hecho!")
        # Reemplaza los guiones bajos por la letra adivinada en todas sus posiciones
        for indice in range(len(palabra_secreta)):
            if palabra_secreta[indice] == letra_ingresada:
                letras_reveladas[indice] = letra_ingresada
    else:
        # Si la letra no está se reduce el número de intentos
        print("MAL.")
        numero_intentos -= 1
        print("Te quedan", numero_intentos, "intentos.")

# Si se acaban los intentos se muestra la palabra correcta
if numero_intentos == 0:
    print("CAGASTE, la palabra era:", palabra_secreta)
