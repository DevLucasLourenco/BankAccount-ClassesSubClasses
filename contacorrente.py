import locale
locale.setlocale(locale.LC_MONETARY, '')


class ContaCorrente():
    
    def __init__(self, nome:str, cpf:str):            
        self.nome = nome.title()
        self.cpf = self._adaptar_cpf(cpf)
        self.saldo = 0
        self.limite = None
    
    
    def _adaptar_cpf(self, item):
        if len(item) == 11:
            item = '{}{}{}.{}{}{}.{}{}{}-{}{}'.format(*item)
        
        elif len(item) == 14:
            pass
        
        return item
    
    
    def _formatar_moeda(self, valor):
        return locale.currency(valor, grouping=True)
    
    
    def consultar_saldo(self):
        print(f'Olá, {self.nome}! O seu salto é de {self._formatar_moeda(self.saldo)}')
        
        return self.saldo
        

    def depositar(self, valor):
        print(f'Olá,{self.nome}! Foi feito um depósito de {self._formatar_moeda(valor)}')
        
        self.saldo += valor
        
        return self.saldo

        
    def _limite_conta(self):
        self.limite = -1000
        
        return self.limite
    

    def sacar(self, valor):
        if self.saldo - valor >= self._limite_conta():
            self.saldo -= valor
            print(f'Olá,{self.nome}! Foi sacado da sua conta o valor de {self._formatar_moeda(valor)}')
            
        else:
            print('Você não tem saldo o suficiente para sacar este valor.')
        
        return self.saldo


    def consultar_limite_ChequeEspecial(self):
        print(f'O seu limite de Cheque Especial é de {self._formatar_moeda(self._limite_conta())}')




