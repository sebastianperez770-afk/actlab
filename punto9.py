'''
Crea una clase llamada Juego que tenga atributos nombre,
género y precio. Implementa un método que muestre la información
del juego y otro que verifique si el juego está en oferta (si el precio es menor a un valor dado).
'''

class Juego:
    def __init__(self, nombre, genero, precio):
        self._nombre = nombre
        self._genero = genero
        self._precio = precio
        
    def getNombre(self):
        return self._nombre
    
    def getGenero(self):
        return self._genero
    
    def getPrecio(self):
        return self._precio
    
    def setNombre(self, nombre):
        self._nombre = nombre
        
    def setGenero(self, genero):
        self._genero = genero
        
    def setPrecio(self, precio):
        self._precio = precio
        
    def isOferta(self, preOriginal):
        if self._precio < preOriginal:
            print(f"El precio está en oferta.")
        else:
            print(f"El precio no está en oferta.")
            
    def showInfo(self):
        print(f"Nombre: {self._nombre}, genero: {self._genero}, precio: {self._precio}")
        