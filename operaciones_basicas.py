"""Modulo de operaciones basicas y calculo de promedio.

Este modulo contiene dos clases:
- OperacionesBasicas: permite realizar operaciones de suma y resta.
- CalculadoraPromedio: calcula el promedio de una lista de valores.
"""


class OperacionesBasicas:
    """Clase para realizar operaciones basicas como suma y resta."""

    def __init__(self):
        """Inicializa la clase con un resultado en 0."""
        self.resultado = 0

    def sumar(self, a, b):
        """Suma dos numeros y almacena el resultado."""
        self.resultado = a + b

    def restar(self, a, b):
        """Resta dos numeros y almacena el resultado."""
        self.resultado = a - b

    def obtener_resultado(self):
        """Devuelve el resultado de la ultima operacion."""
        return self.resultado


def obtener_cantidad_valores(self):
    """Devuelve la cantidad de valores en la lista."""
    return len(self.valores)

    def __init__(self, valores):
        """Inicializa la clase con una lista de valores."""
        self.valores = valores

    def calcular_promedio(self):
        """Calcula y devuelve el promedio de la lista de valores."""
        if not self.valores:
            return 0
        return sum(self.valores) / len(self.valores)


# Variables globales
NUMEROS = [1, 2, 3, 4, 5]
NUM1 = 10
NUM2 = 20


# Ejecución principal
if __name__ == "__main__":
    # Usar la clase OperacionesBasicas
    operaciones = Operaciones_Basicas()
    operaciones.sumar(NUM1, NUM2)
    print(f"El resultado de la suma es: {operaciones.obtener_resultado()}")

    operaciones.restar(NUM1, NUM2)
    print(f"El resultado de la resta es: {operaciones.obtener_resultado()}")

    # Usar la clase CalculadoraPromedio
    calculadora_promedio = CalculadoraPromedio(NUMEROS)
    promedio_resultado = calculadora_promedio.calcular_promedio()
    print(f"El promedio de los numeros es: {promedio_resultado}")
