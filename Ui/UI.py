from Modelo.Modelo import Cuenta

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