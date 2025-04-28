# Clase que representa un paciente con sus datos principales
class Paciente:
    def __init__(self, nombre, edad, sintoma, prioridad):
        self.nombre = nombre
        self.edad = edad
        self.sintoma = sintoma
        self.prioridad = prioridad
        self.siguiente = None

    def __str__(self):
        # Representación en texto del paciente
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Síntoma: {self.sintoma}, Prioridad: {self.prioridad}"

# Clase que gestiona la clínica y la cola de pacientes
class Clinica:
    def __init__(self):
        # Lista que actúa como cola de pacientes
        self.frente = None

    def ingresar_paciente(self, nombre, edad, sintoma, prioridad):
        nuevo_paciente = Paciente(nombre, edad, sintoma, prioridad)
         # Si la lista está vacía o el nuevo paciente tiene más prioridad que el frente
        if self.frente is None or nuevo_paciente.prioridad < self.frente.prioridad:
            nuevo_paciente.siguiente = self.frente
            self.frente = nuevo_paciente
        else:
             # Busca la posición correcta donde insertar el nuevo paciente
            actual = self.frente
            while actual.siguiente is not None and actual.siguiente.prioridad <= nuevo_paciente.prioridad:
                actual = actual.siguiente

            nuevo_paciente.siguiente = actual.siguiente
            actual.siguiente = nuevo_paciente

              # Aca inserta el nuevo paciente en la posición encontrada

        print(f"Paciente {nombre} ingresado correctamente.")

    def mostrar_pacientes(self):
        if self.frente is None: 
            print("No hay pacientes en espera.")
        else:
            print("\nLista de pacientes por orden de prioridad:")
            actual = self.frente
            idx = 1
            while actual:
                print(f"{idx}. {actual}") ## Usa el método __str__ de Paciente para mostrar info
                actual = actual.siguiente # Avanza al siguiente paciente
                idx += 1
    def atender_paciente(self):
        if self.frente is None:
             print("No hay pacientes para atender.")
        else:
            paciente_atendido = self.frente  # El frente avanza al siguiente paciente
            self.frente = self.frente.siguiente
            print(f"Paciente atendido: {paciente_atendido.nombre}")
    
      