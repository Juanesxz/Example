class Coche:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
    
    def carro(self):
        return print(self.marca, self.modelo)
    def prendido(self):
       self.encendido = True
       return self.encendido
    def apagado(self):
        self.encendido = False
        return self.encendido

carros = Coche("Ferrari","V2")
carros.carro()
print(carros.prendido())
print(carros.apagado())


