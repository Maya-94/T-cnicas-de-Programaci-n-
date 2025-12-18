# archivo: banco.py

class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
        print(f"Depósito exitoso. Saldo actual: ${self.saldo}")

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro exitoso. Saldo actual: ${self.saldo}")
        else:
            print("Fondos insuficientes")


# Programa principal
cuenta1 = CuentaBancaria("Juan Pérez", 100)
cuenta1.depositar(50)
cuenta1.retirar(30)
