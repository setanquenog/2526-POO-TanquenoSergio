class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria.
    """

    def __init__(self, numero_cuenta, titular, saldo_inicial=0.0):
        """
        CONSTRUCTOR (__init__)
        Se ejecuta automáticamente al crear un objeto CuentaBancaria.
        Inicializa los atributos básicos de la cuenta.
        """
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo_inicial

        print(f"[INIT] Cuenta creada para {self.titular} con saldo inicial ${self.saldo}")

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito realizado: ${monto}. Nuevo saldo: ${self.saldo}")

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro realizado: ${monto}. Nuevo saldo: ${self.saldo}")
        else:
            print("Fondos insuficientes.")

    def mostrar_datos(self):
        print("----- DATOS DE LA CUENTA -----")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: ${self.saldo}")

    def __del__(self):
        """
        DESTRUCTOR (__del__)
        Se ejecuta cuando el objeto es eliminado de la memoria.
        Simula el cierre de la cuenta o liberación de recursos.
        """
        print(f"[DEL] La cuenta de {self.titular} ha sido cerrada y liberada de memoria.")

