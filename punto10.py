'''
Crea una clase llamada Circulo que tenga un atributo radio.
Implementa métodos para calcular el área y la circunferencia del círculo,
y asegúrate de que el radio no pueda ser negativo.
'''

import math

class Circulo:
    def __init__(self, radio):
        if radio > 0:
            self._radio = radio
        
    def getRadio(self):
        return self._radio
    
    def setRadio(self, radio):
        if radio > 0:
            self._radio = radio
            
    def calArea(self):
        return math.pi * self._radio ** 2
    
    def calCircunferencia(self):
        return 2 * math.pi * self._radio
        
    