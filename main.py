import contacorrente
import Agencias


conta = contacorrente.ContaCorrente('lucas lourenco','12345678912', 123456)

conta.depositar(22000)
conta.consultar_limite_ChequeEspecial()
conta.sacar(10000)
conta.consultar_saldo()
conta.historico_transacoes()

print('-'*20)

conta_gp = contacorrente.ContaCorrente('bianca', '98765432112', num_conta=456)
conta.transferir(200, conta_gp)
conta.consultar_saldo()
conta_gp.consultar_saldo()




######################################################



conta_lucas = contacorrente.ContaCorrente('lucas lourenco','12345678912',123456)

cartao_lucas = contacorrente.CartaoCredito('Lucas Lourenco', conta_lucas)

print(cartao_lucas.conta_corrente.num_conta)

print(conta_lucas.cartoes[0].numero)

print(cartao_lucas.cod_seguranca)

cartao_lucas.senha = '9876'
print(cartao_lucas.senha)


print(cartao_lucas.__dict__)



#######################################################



