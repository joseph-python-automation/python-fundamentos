print("Bienvenidos al juego de adivina el número")

jugador1 = int(input("Jugador 1 - Ingresa el número secreto (los demás no miren): "))
print("\n" * 30)

entrada = input("Jugador 2 - Intenta adivinar el número: ")
while not entrada.lstrip('-').isdigit():
    print("Entrada inválida. Ingresa un número entero.")
    entrada = input("Jugador 2 - Intenta adivinar el número: ")

jugador2 = int(entrada)

while True:
    if jugador2 == jugador1:
        print("🎉 ¡Felicidades! Has adivinado el número.")
        break
    elif jugador2 < jugador1:
        print("Pista: El número secreto es mayor ↑")
    else:
        print("Pista: El número secreto es menor ↓")

    entrada = input("Intenta de nuevo: ")
    while not entrada.lstrip('-').isdigit():
        print("Entrada inválida. Ingresa un número entero.")
        entrada = input("Intenta de nuevo: ")

    jugador2 = int(entrada)
