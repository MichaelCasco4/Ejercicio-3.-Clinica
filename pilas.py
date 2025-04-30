#Ejercio 2 (Michael Casco)


# Ordena la lista de enteros de mayor a menor 
def ordena(pila):
    lista_ordenada = sorted(pila, reverse=True)
    pila_ordenada = []
    for num in lista_ordenada:
        pila_ordenada.append(num)

    return pila_ordenada


#Validacion de entrada, no se permiten letras, unicamente numeros
def entrada_valida():
    while True:
        entrada = input("Ingresa los numeros y separalos por un espacio: ")
        partes = entrada.strip().split() #Se separa la entrada por espacio y se elimina los posibles espacios extras

        try:
            #Se convierte cada parte en un numero entero
            numeros = [int(x) for x in partes]
            return numeros
        except ValueError:
            print("Entrada invalida, solo se aceptan numeros enteros. Intentalo de nuevo \n")

#Creacion de main, ejecucion del programa
def main():

#Llamamos a la funcion de entrada valida para obtener la pila de numeros 
    pila = entrada_valida()

    print("----Ordenador de pila-----")

    print("\n Pila original (fondo a tope): ")
    print(pila)

#LLamamos a la funcion de ordenar, para que ordene los numeros de mayor a menor
    pila_ordenada = ordena(pila)

    print("\n Pila ordenada (El mayor al fondo y el menor al tope): ")
    print(pila_ordenada)

#Ejecucion del programa
if __name__ == "__main__":
    main()
