class Cuenta:

    def __init__(self, numeroCuenta=None, documentoIdentidad=None, nombreCliente=None, saldoActual=0.0):
        self.__numeroCuenta = numeroCuenta
        self.__documentoIdentidad = documentoIdentidad
        self.__nombreCliente = nombreCliente
        self.__saldoActual = saldoActual

    @property
    def numeroCuenta(self):
        return self.__numeroCuenta

    @property
    def documentoIdentidad(self):
        return self.__documentoIdentidad

    @property
    def nombreCliente(self):
        return self.__nombreCliente

    @property
    def saldoActual(self):
        return self.__saldoActual

    def depositarDinero(self, monto):
        retencion = monto * 0.19
        montoNeto = monto - retencion
        self.__saldoActual += montoNeto

    def retirarDinero(self, monto):
        if monto <= self.__saldoActual:
            self.__saldoActual -= monto
        else:
            print("Saldo insuficiente")

    def mostrarDatos(self):
        print(f"Número de cuenta: {self.__numeroCuenta}")
        print(f"Documento de identidad: {self.__documentoIdentidad}")
        print(f"Nombre del cliente: {self.__nombreCliente}")
        print(f"Saldo actual: {self.__saldoActual}")