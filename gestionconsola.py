opcion = ""
elementos = []

while opcion != "3":
    print("\n1. Agregar elemento")
    print("2. Ver elementos")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        item = input("Ingresa un elemento: ")
        elementos.append(item)
        print("Elemento agregado ✅")

    elif opcion == "2":
        if elementos:
            print("Lista de elementos:")
            for e in elementos:
                print("-", e)
        else:
            print("La lista está vacía 📭")

    elif opcion == "3":
        print("Saliendo del programa 👋")

    else:
        print("Opción inválida ❌")
