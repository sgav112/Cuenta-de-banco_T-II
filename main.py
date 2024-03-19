from UI import mostrarMenu, crearCuenta, depositarDinero, retirarDinero, mostrarDatosCuenta

def main():
    cuentaClientes = []

    while True:
        mostrarMenu()
        opcion = int(input("Ingrese la opción deseada: "))
        if opcion == 1:
            crearCuenta(cuentaClientes)
        elif opcion == 2:
            depositarDinero(cuentaClientes)
        elif opcion == 3:
            retirarDinero(cuentaClientes)
        elif opcion == 4:
            mostrarDatosCuenta(cuentaClientes)
        elif opcion == 5:
            break


if __name__ == "__main__":
    main()