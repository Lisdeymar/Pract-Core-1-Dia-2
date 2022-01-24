from CuentaBancaria import CuentaBancaria

alex = CuentaBancaria( 0.01, 100 )
ana = CuentaBancaria( 0.01, 200 )

alex.depósito(5).depósito(10).depósito(20).retiro(30).generar_interés().mostrar_info_cuenta()
ana.depósito(200).depósito(350).retiro(10).retiro(15).retiro(20).retiro(25).generar_interés().mostrar_info_cuenta()

CuentaBancaria.imprimir_cuentas()


