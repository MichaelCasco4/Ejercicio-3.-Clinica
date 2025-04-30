from Ejercicio1 import Pila

def separarParImpar(pila_original):
    pila_par = Pila()
    pila_impar = Pila()

    while pila_original.cabeza is not None:
        nodo_extraido = pila_original.pop()
        if nodo_extraido.dato % 2 == 0:
            pila_par.push(nodo_extraido.dato)
        else:
            pila_impar.push(nodo_extraido.dato)
    print("Lista par:")
    pila_par.imprimir()
    print("Lista impar:")
    pila_impar.imprimir()
        


if __name__ == "__main__":
    pila = Pila()
    while True: 
        try:
            numero = int(input("Digite un número a ingresar: "))
            pila.push(numero)
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")


        opc = input("Desea ingresar mas numeros (y/n)")
        if opc.lower() == "n":
            separarParImpar(pila)
            break
        
    
    
