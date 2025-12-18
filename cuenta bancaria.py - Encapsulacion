class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular
        self.__saldo = saldo_inicial  # atributo privado

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto

    def obtener_saldo(self):
        return self.__saldo


# Ejemplo
if __name__ == "__main__":
    cuenta = CuentaBancaria("María", 500)
    cuenta.depositar(200)
    cuenta.retirar(100)
    print("Saldo final:", cuenta.obtener_saldo())
