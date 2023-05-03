class Calculadora:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]

    def ingreso(self):
        self.datos = [
            int(input("ingresar datos" + str(i + 1) + "=")) for i in range(self.n)
        ]


class operaciones(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 2)

    def suma(self):
        a, b = self.datos
        suma = a + b
        print("el rescultado es:", suma)

    def resta(self):
        a, b = self.datos
        resta = a - b
        print("el rescultado es:", resta)


class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 1)

    def cuadrada(self):
        import math

        (a,) = self.datos
        print("el resultado es:", math.sqrt(a))


ejemplo = raiz()
ejemplo.ingreso()
ejemplo.cuadrada()