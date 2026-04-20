'''
Crea una clase llamada Auto que tenga los siguientes atributos:
marca, modelo y año. Implementa un método que muestre la información
del coche en un formato legible.
'''

class Auto:
    def __init__(self, marca, modelo, year):
        self._marca = marca
        self._modelo = modelo
        self._year = year
    
    def getMarca(self):
        return self._marca
    
    def getModelo(self):
        return self._modelo

    def getYear(self):
        return self._year
    
    def setMarca(self, newMarca):
        self._marca = newMarca
        
    def setModelo(self, newModelo):
        self._modelo = newModelo
        
    def setYear(self, newYear):
        if not newYear > 1885:
            print("El año ingresado es inválido.")
        else:
            self._year = newYear
    
    def showInfo(self):
        print(f"La marca del auto es {self._marca}, modelo {self._modelo} y es del año {self._year}.")
        