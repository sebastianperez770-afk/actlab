'''
Crea una clase llamada Libro con atributos titulo,
autor y año_publicacion. Implementa un método que
devuelva una descripción del libro y otro que verifique
si el libro es considerado un clásico (publicado hace más de 50 años).
'''

import datetime

class Libro:
    def __init__(self, titulo, autor, yearPub):
        self._titulo = titulo
        self._autor = autor
        self._yearPub = yearPub
        
    def getTitulo(self):
        return self._titulo
    
    def getAutor(self):
        return self._autor
    
    def getYearPub(self):
        return self._yearPub
    
    def setTitulo(self, titulo):
        self._titulo = titulo
        
    def setAutor(self, autor):
        self._autor = autor
        
    def setYearPub(self, yearPub):
        self._yearPub = yearPub
        
    def libroDescripcion(self):
        print(f"El libro es {self._titulo}, su autor es {self._autor} y fue publicado el año {self._yearPub}")
        
    def esClasico(self):
        if 
        
        