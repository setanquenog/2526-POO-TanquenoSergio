from modelos.cuenta_bancaria import CuentaBancaria

class BancoServicio:
    """
    Clase que gestiona las operaciones del banco.
    """

    def crear_cuenta(self, numero, titular, saldo):
        """
        Crea y devuelve un objeto CuentaBancaria.
        """
        return CuentaBancaria(numero, titular, saldo)

    def operar_cuenta(self, cuenta):
        """
        Ejecuta operaciones básicas sobre la cuenta.
        """
        cuenta.mostrar_datos()
        cuenta.depositar(100)
        cuenta.retirar(600)

