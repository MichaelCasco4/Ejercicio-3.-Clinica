from modulos import Clinica,Paciente

# Función principal que maneja el menú interactivo de la clínica
def menu():
    clinica = Clinica()
    while True:
        print("\n--- Menú Clínica ---")
        print("1. Ingresar nuevo paciente")
        print("2. Mostrar pacientes en espera")
        print("3. Atender paciente")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Solicitar datos del paciente y validar entradas
            nombre = input("Nombre completo: ")
            try:
                edad = int(input("Edad: "))
                if edad <= 0:
                    print("La edad debe ser un número positivo.")
                    continue
            except ValueError:
                print("Edad inválida. Debe ser un número.")
                continue

            sintoma = input("Síntoma principal: ")

            try:
                prioridad = int(input("Prioridad (1-5): "))
                if prioridad < 1 or prioridad > 5:
                    print("La prioridad debe estar entre 1 y 5.")
                    continue
            except ValueError:
                print("Prioridad inválida. Debe ser un número entre 1 y 5.")
                continue

            clinica.ingresar_paciente(nombre, edad, sintoma, prioridad)

        elif opcion == "2":
            # Mostrar pacientes en espera
            clinica.mostrar_pacientes()
        elif opcion == "3":
            # Atender al primer paciente en la cola
            clinica.atender_paciente()
        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    menu()