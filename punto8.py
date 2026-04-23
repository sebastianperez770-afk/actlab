'''
Crea una clase llamada Producto que tenga atributos nombre,
precio y stock. Implementa métodos para aumentar y disminuir
el stock, asegurándote de que no se pueda tener un stock negativo.
'''

class Producto:
    def __init__(self, nombre, precio, stock):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock
        
    def getNombre(self):
        return self._nombre
    
    def getPrecio(self):
        return self._precio
    
    def getStock(self):
        return self._stock
    
    def setNombre(self, nombre):
        self._nombre = nombre
        
    def setPrecio(self, precio):
        self._precio = precio
        
    def setStock(self, stock):
        self._stock = stock
        
    def disStock(self, num):
        if self._stock - num > 0:
            self._stock -= num
        else:
            print("Stock insuficiente.")
            
    def aumStock(self, num):
        self._stock += num
        