def Convbinario(numero):
    pila = []

    if numero == 0:
        pila.append(0)
    else:
        while numero > 0:
            residuo = numero % 2
            pila.append(residuo)
            numero //= 2

    # Convertimos la pila de bits a binario (como string)
    binario = ''.join(str(bit) for bit in reversed(pila))
    return binario


# Aquí sí usamos una pila real (LIFO)
pila_binarios = []

while True:
    print("\n--- MENÚ ---")
    print("1. Convertir número a binario (Push)")
    print("2. Mostrar valores de la pila")
    print("3. Desapilar último binario (Pop)")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        try:
            n = int(input("Ingrese un número entero: "))
            binario = Convbinario(n)
            pila_binarios.append(binario)
            print(f"El número en binario es: {binario}")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    elif opcion == "2":
        if not pila_binarios:
            print("La pila está vacía.")
        else:
            print("Valores en la pila (último arriba):")
            for binario in reversed(pila_binarios):
                print(binario)

    elif opcion == "3":
        if not pila_binarios:
            print("La pila ya está vacía.")
        else:
            eliminado = pila_binarios.pop()
            print(f"Elemento desapilado: {eliminado}")

    elif opcion == "4":
        print("Saliendo del programa.")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
