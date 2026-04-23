'''
Crea una clase llamada Estudiante que tenga atributos como nombre,
edad y notas (una lista de números). Implementa métodos
para agregar una nota y calcular el promedio de las notas.
'''

class Estudiante:
    def __init__(self, nombre, edad, notas):
        self._nombre = nombre
        self._edad = edad
        self._notas = notas
        
    def getNombre(self):
        return self._nombre
    
    def getEdad(self):
        return self._edad
    
    def getNotas(self):
        return self._notas
    
    def setNombre(self, nombre):
        self._nombre = nombre
        
    def setEdad(self, edad):
        self._edad = edad
        
    def setNotas(self, notas):
        self._notas = notas
    
    def addNota(self, newNota):
        self._notas.append(newNota)
    
    def calPromedio(self):
        suma = sum(self._notas)
        promedio = suma / len(self._notas)
        return promedio
            
