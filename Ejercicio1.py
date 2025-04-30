class nodo:
    def __init__(self, dato):
        # Inicializa un nodo con un valor y una referencia al siguiente (inicialmente nula)
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        # Crea una pila vacía utilizando una lista enlazada
        self.cabeza = None

    def push(self, valor):
        # Agrega un nuevo elemento en la cima de la pila
        valor = nodo(valor)
        valor.siguiente = self.cabeza
        self.cabeza = valor

    def pop(self):
        # Elimina y retorna el elemento en la cima de la pila
        if self.cabeza is None:
            return None
        nodo_eliminado = self.cabeza
        self.cabeza = self.cabeza.siguiente #Reasigna el nuevo tope de la pila
        return nodo_eliminado

    def imprimir(self):
        # Imprime todos los elementos de la pila desde la cima hacia abajo
        temporal = self.cabeza
        while temporal:
            print(temporal.dato)
            temporal = temporal.siguiente
