"""
Creare una cuenta bancarica utilizando class. Poseera el deposito y retiro.
Tambien habra un titular y saldo.
"""

class Cuenta_Bancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def Deposito(self, cantidad):
        self.saldo += cantidad
        print("Se deposito: ", cantidad)
    def Retirar(self, retirar):
        self.saldo -= retirar
        print("Se retiro: ", retirar)

    def mostrar(self):
        print(self.__dict__)

cuenta1 = Cuenta_Bancaria('Jose', 1500000)
cuenta1.mostrar()
cuenta1.Deposito(300000)
cuenta1.mostrar()
cuenta1.Retirar(150000)
cuenta1.mostrar()

