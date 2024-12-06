from model.operacion import Operacion
from view.vista_calculadora import Vista


class Controlador:
    def __init__(self):
        self.vista = Vista()

    def iniciar(self):
        while True:
            self.vista.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion in ["1", "2", "3", "4"]:
                self.realizar_operacion(opcion)
            elif opcion == "5":
                self.ver_historial()
            elif opcion == "6":
                print("Gracias por usar la calculadora. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def realizar_operacion(self, opcion):
        operaciones = {
            "1": "suma",
            "2": "resta",
            "3": "multiplicacion",
            "4": "division"
        }
        tipo_operacion = operaciones[opcion]

        numero1, numero2 = self.vista.solicitar_numeros()
        if numero1 is None or numero2 is None:
            return

        
