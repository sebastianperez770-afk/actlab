'''
Crea una clase llamada Persona con atributos nombre,
edad y sexo. Implementa un método que permita cambiar
la edad de la persona y otro que muestre la información de la persona.
'''

class Persona:
    def __init__(self, nombre, edad, sexo):
        self._nombre = nombre
        self._edad = edad
        self._sexo = sexo
        
    def getEdad(self):
        return self._edad
    
    def getNombre(self):
        return self._nombre
    
    def getSexo(self):
        return self._sexo
    
    def setNombre(self, newNombre):
        self._nombre = newNombre
        
    def setSexo(self, newSexo):
        self._sexo = newSexo
    
    def cambiarEdad(self, newEdad):
        if newEdad > 0:
            self._edad = newEdad
        else:
            print("Edad inválida")
            
    def showInfo(self):
        print(f"La persona se llama {self._nombre}, tiene {self._edad} años y su sexo es {self._sexo}")
        