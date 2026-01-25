from servicios.banco_servicio import BancoServicio


def main():
    print("=== SISTEMA DE CUENTAS BANCARIAS ===")

    banco = BancoServicio()

    # Aquí se ejecuta el CONSTRUCTOR (__init__)
    cuenta1 = banco.crear_cuenta("001", "Ana López", 500)

    banco.operar_cuenta(cuenta1)

    print("\nFin del programa.")

    # Al eliminar el objeto, se ejecuta el DESTRUCTOR (__del__)
    del cuenta1


if __name__ == "__main__":
    main()