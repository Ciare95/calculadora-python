from mysql.connector import Error
from model.database_connection import DatabaseConnection  


class Operacion:
    @staticmethod
    def realizar_operacion(numero1, numero2, tipo_operacion):
        if tipo_operacion == "suma":
            return numero1 + numero2
        elif tipo_operacion == "resta":
            return numero1 - numero2
        elif tipo_operacion == "multiplicacion":
            return numero1 * numero2
        elif tipo_operacion == "division":
            if numero2 == 0:
                raise ZeroDivisionError("El divisor no puede ser cero.")
            return numero1 / numero2
        else:
            raise ValueError("Operación no válida.")

    
