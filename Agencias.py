from random import randint


class Agencia:
    
    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 1000000
        self.emprestimos = []
        
        
    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'O Caixa da agência está abaixo do mínimo. Caixa atual: {self.caixa}')
            
        else:
            print(f'O valor do caixa está OK. Caixa atual: {self.caixa}')
            
    
    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
            self.caixa -= valor
            
            print(f'Foi feito um emprestimo para o CPF: {cpf}, no valor de {valor}. Terá um juros de {juros}\nO valor atual do caixa é de {self.caixa}')
            
        else:
            print('Emprestimo não é possível. Dinheiro não disponível em caixa.')
            

    def adicionar_cliente(self, cliente_nome, cpf, patrimonio):            
        self.clientes.append((cliente_nome, cpf, patrimonio))
        

        
    
class AgenciaVirtual(Agencia):
    
    def __init__(self): 
        self.site = 'www.DevLucasAgenciaVirtual.com.br'
        super().__init__('2133333333', '123456789', '0001')
        self.caixa = 1500000
        self.caixa_paypal = 0
    
    
    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor
    
    
    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor
        
        
    
class AgenciaComum(Agencia):
    
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero = randint(1000,9999))
        self.caixa = 2000000
        
    
    
class AgenciaPremium(Agencia):
    
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero = randint(1000,9999))
        self.caixa = 100000000
        
        
    def adicionar_cliente(self, cliente_nome, cpf, patrimonio):
        
        if patrimonio > 500000:
            super().adicionar_cliente(cliente_nome, cpf, patrimonio)
            
        else:
            print(f'O cliente {cliente_nome} não possui patrimônio para para entrar na Agencia Premium. Patrimônio de {patrimonio}')    
            
            
if __name__ == '__main__':
    

    print('='*80)
    agencia = Agencia('21999999999', '14984984944494', '123')

    agencia.verificar_caixa()

    agencia.emprestar_dinheiro(900, '999.999.999-99', 0.6)

    agencia.adicionar_cliente('lucas lourenco','12345678999', 1944894)
    print(agencia.clientes)

    ################################################################################
    print('='*80)

    agencia_virtual = AgenciaVirtual()
    agencia_virtual.verificar_caixa()
    print(agencia_virtual.site)
    print(agencia_virtual.__dict__)

    agencia_virtual.depositar_paypal(20000)
    agencia_virtual.sacar_paypal(1000)

    agencia_virtual.verificar_caixa()
    ################################################################################
    print('='*80)

    agencia_premium = AgenciaPremium('213654987','4848949854')
    agencia_premium.verificar_caixa()
    agencia_premium.adicionar_cliente('Lucas Lourenco','12345678999', 999999999999)
    print(agencia_premium.clientes)

    print('='*80)
    ################################################################################
    agencia_comum = AgenciaComum('21456789123','123456000000')
    agencia_comum.verificar_caixa()
        