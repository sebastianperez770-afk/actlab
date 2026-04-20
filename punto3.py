'''
Crea una clase llamada CuentaBancaria que tenga
atributos como titular, saldo y numero_cuenta.
Implementa métodos para depositar y retirar dinero,
asegurándote de que el saldo no se vuelva negativo.
'''

class CuentaBancaria:
    def __init__(self, titular, saldo, numeroCuenta):
        self._titular = titular
        self._saldo = saldo
        self._numeroCuenta = numeroCuenta
        
    def getTitular(self):
        return self._titular
    
    def getSaldo(self):
        return self._saldo
    
    def getNumCuenta(self):
        return self._numeroCuenta
    
    def setTitular(self, newTitular):
        self._titular = newTitular
        
    def setSaldo(self, newSaldo):
        self._saldo = newSaldo
        
    def setNumCuenta(self, newNumCuenta):
        self._numeroCuenta = newNumCuenta
    
    def depositarDinero(self, dinero):
        if dinero > 0:
            self._saldo += dinero
        else:
            print("El dinero introducido es inválido")
            
    def retirarDinero(self, dinero):
        if self._saldo - dinero >= 0:
            self._saldo - dinero
            return dinero
        else:
            print("Saldo insuficiente.")
    