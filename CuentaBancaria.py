class CuentaBancaria:
    cuentas = []
    #Constructor
    def __init__(self, tasa_interés= 0.01, balance=0 ):
        #Atributos son variables con alcance dentro de la clase
        self.tasa_interés = tasa_interés
        self.balance = balance
        CuentaBancaria.cuentas.append(self)
    
#aumenta el balance de la cuenta en el monto dado
    def depósito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else: 
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        return self
        
    def mostrar_info_cuenta(self):
        print(f"Balance: {self.balance}" )
        return self

    def generar_interés(self):
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_interés)
        return self

    @classmethod
    def imprimir_cuentas(cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_info_cuentas()





            