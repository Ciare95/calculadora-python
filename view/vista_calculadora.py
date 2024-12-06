class Vista:
    def mostrar_menu(self):
        print("--- Menú de Calculadora ---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Ver historial")
        print("6. Salir")

    def solicitar_numeros(self):
        try:
            numero1 = float(input("Ingrese el primer número: "))
            numero2 = float(input("Ingrese el segundo número: "))
            return numero1, numero2
        except ValueError:
            print("Error: Ingrese números válidos.")
            return None, None

    def mostrar_resultado(self, resultado):
        print(f"El resultado de la operación es: {resultado}")

    
    def mostrar_error(self, mensaje):
        print(f"Error: {mensaje}")
