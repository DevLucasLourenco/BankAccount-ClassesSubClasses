import contacorrente


conta = contacorrente.ContaCorrente('lucas lourenco','12345678912')

conta.depositar(22000)
conta.consultar_limite_ChequeEspecial()
conta.sacar(10000)
conta.consultar_saldo()