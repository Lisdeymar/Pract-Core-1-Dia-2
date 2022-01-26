from CuentaBancaria import CuentaBancaria, Usuario

ahorro = CuentaBancaria( 0.01, 100 )
creditos = CuentaBancaria( 0.02, 200 )

ahorro.depósito(5).depósito(10).depósito(20).retiro(30).generar_interés().mostrar_info_cuenta()
creditos.depósito(200).depósito(350).retiro(10).retiro(15).retiro(20).retiro(25).generar_interés().mostrar_info_cuenta()

CuentaBancaria.imprimir_cuentas()

ana = Usuario("ana")

ana.cuenta['ahorro'].depósito(100)
ana.mostrar_balance_usuario()

