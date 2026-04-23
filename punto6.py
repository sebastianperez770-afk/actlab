'''
Crea una clase llamada Rectángulo que tenga atributos
base y altura. Implementa métodos para calcular el área y el perímetro del rectángulo.
'''

class Rectangulo:
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura
        
    def getBase(self):
        return self._base

    def getAltura(self):
        return self._altura
    
    def setBase(self, base):
        self._base = base
        
    def setAltura(self, altura):
        self._altura = altura
        
    def calArea(self):
        return self._base * self._altura
    
    def calPerimetro(self):
        return self._base * 2 + self._altura * 2
    