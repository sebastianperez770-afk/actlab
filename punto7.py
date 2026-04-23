'''
Crea una clase llamada Empleado con atributos nombre,
salario y departamento. Implementa un método que aumente
el salario en un porcentaje dado y otro que muestre la información del empleado.
'''

class Empleado:
    def __init__(self, nombre, salario, departamento):
        self._nombre = nombre
        self._salario = salario
        self._departamento = departamento
        
    def getNombre(self):
        return self._nombre
    
    def getSalario(self):
        return self._salario
    
    def getDepartamento(self):
        return self._departamento
    
    def setNombre(self, nombre):
        self._nombre = nombre
        
    def setSalario(self, salario):
        self._salario = salario
    
    def setDepartamento(self, departamento):
        self._departamento = departamento
        
    def aumSalario(self, porcentaje):
        porcen = porcentaje / 100
        porcen += 1
        self._salario = self._salario * porcen

        
    def showInfo(self):
        print(f"Nombre: {self._nombre}, salario: {self._salario}, departamento: {self._departamento}")
        