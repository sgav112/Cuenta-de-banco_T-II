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

def mostrarMenu():
    print("-" * 20)
    print("   Banco del Pueblo")
    print("-" * 20)
    print("1. Crear cuenta")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Mostrar datos de la cuenta")
    print("5. Salir")
    print("-" * 20)

def crearCuenta(cuentaClientes):
    numeroCuenta = int(input("Ingrese el número de cuenta: "))
    documentoIdentidad = int(input("Ingrese el documento de identidad: "))
    nombreCliente = input("Ingrese el nombre del cliente: ")
    saldoActual = float(input("Ingrese el saldo actual: "))
    cuenta = Cuenta(numeroCuenta, documentoIdentidad, nombreCliente, saldoActual)
    cuentaClientes.append(cuenta)

def depositarDinero(cuentaClientes):
    numeroCuenta = int(input("Ingrese el número de cuenta: "))
    monto = float(input("Ingrese el monto a depositar: "))
    cuenta = buscarCuenta(numeroCuenta, cuentaClientes)
    if cuenta:
        cuenta.depositarDinero(monto)
        print("Deposito realizado exitosamente")
    else:
        print("Cuenta no encontrada")

def retirarDinero(cuentaClientes):
    numeroCuenta = int(input("Ingrese el número de cuenta: "))
    monto = float(input("Ingrese el monto a retirar: "))
    cuenta = buscarCuenta(numeroCuenta, cuentaClientes)
    if cuenta:
        cuenta.retirarDinero(monto)
    else:
        print("Cuenta no encontrada")

def mostrarDatosCuenta(cuentaClientes):
    numeroCuenta = int(input("Ingrese el número de cuenta: "))
    cuenta = buscarCuenta(numeroCuenta, cuentaClientes)
    if cuenta:
        cuenta.mostrarDatos()
    else:
        print("Cuenta no encontrada")

def buscarCuenta(numeroCuenta, cuentaClientes):
    for cuenta in cuentaClientes:
        if cuenta.numeroCuenta == numeroCuenta:
            return cuenta
    return None