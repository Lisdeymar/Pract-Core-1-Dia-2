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
            cuenta.mostrar_info_cuenta()

class Usuario:

    def __init__(self, nombre):
        self.nombre = nombre
        self.cuenta = {
            "ahorros" : CuentaBancaria(0.01,100),
            "creditos" : CuentaBancaria(0.02,200)
        }
        
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre}, ahorro Balance: {self.cuenta['ahorro'].mostrar_info_cuenta}")
        print(f"Usuario: {self.nombre}, creditos Balance: {self.cuenta['creditos'].mostrar_info_cuenta)}")
        return self

    def transfer_money(self,depósito,usuario):
        self.depósito -= depósito
        usuario.depósito += depósito
        self.mostrar_balance_usuario()
        usuario.mostrar_balance_usuario()
        return self


adrien = Usuario("Adrien")

adrien.cuenta['checking'].depósito(100)
adrien.mostrar_balance_usuario()




            