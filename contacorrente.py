import random
from datetime import datetime
import pytz
import locale
locale.setlocale(locale.LC_MONETARY, '')

class ContaCorrente():
    '''
    Cria um objeto ContaCorrente para as contas dos clientes.
    
    Atributos:
        nome: Nome do Cliente
        cpf: CPf do cliente
    '''
       
    def __init__(self, nome:str, cpf:str,  num_conta:int):            
        
        self.nome = nome.title()
        self.cpf = ContaCorrente._adaptar_cpf(cpf)
        self.num_conta = num_conta
        self._saldo = 0
        self._limite = None
        self._transacoes = []
        self.cartoes = []
        

        
    @staticmethod
    def _data_hora():
        fuso_horario = pytz.timezone('Brazil/West')
        horario = datetime.now(fuso_horario)
        return horario.strftime('%d-%m-%Y %H:%M:%S')
    
    
    @staticmethod
    def _adaptar_cpf(item):
        if len(item) == 11:
            item = '{}{}{}.{}{}{}.{}{}{}-{}{}'.format(*item)
        
        elif len(item) == 14:
            pass
        
        return item
    
    
    @staticmethod
    def _formatar_moeda(valor):
        return locale.currency(valor, grouping=True)
    
    
    def consultar_saldo(self):
        print(f'Olá, {self._nome}! O seu salto é de {ContaCorrente._formatar_moeda(self._saldo)}')
        
        return self._saldo
        

    def depositar(self, valor):
        print(f'Olá, {self._nome}! Foi feito um depósito de {ContaCorrente._formatar_moeda(valor)}')
        
        self._saldo += valor
        self._transacoes.append(f'Valor: {valor} | Saldo: {self._saldo} | Data e Horario: {ContaCorrente._data_hora()}')
        
        return self._saldo

        
    def _limite_conta(self):
        self._limite = -1000
        
        return self._limite
    

    def sacar(self, valor):
        if self._saldo - valor >= self._limite_conta():
            self._saldo -= valor
            print(f'Olá, {self._nome}! Foi sacado da sua conta o valor de {ContaCorrente._formatar_moeda(valor)}')
            self._transacoes.append(f'Valor: {- valor} | Saldo: {self._saldo} | Data e Horario: {ContaCorrente._data_hora()}')
            
        else:
            print('Você não tem saldo o suficiente para sacar este valor.')
        
        return self._saldo


    def consultar_limite_ChequeEspecial(self):
        print(f'O seu limite de Cheque Especial é de {ContaCorrente._formatar_moeda(self._limite_conta())}')
        
    
        
    def historico_transacoes(self):
        print('Histórico de Transacoes:')
        for transacao in self._transacoes:
            print(transacao)
        
    
    def transferir(self, valor, caonta_destino:object):
        self._saldo -= valor
        self._transacoes.append(f'Valor: {valor} | Saldo: {self._saldo} | Data e Horario: {ContaCorrente._data_hora()}')
        caonta_destino._saldo += valor
        caonta_destino._transacoes.append(f'Valor: {valor} | Saldo: {caonta_destino._saldo} | Data e Horario: {ContaCorrente._data_hora()}')
        
        

class CartaoCredito:
    
    def __init__(self, titular, conta_corrente):
        self.numero = 123
        self.titular = titular
        self.data_validade= '{}/{}'.format(CartaoCredito._data_validade().month, CartaoCredito._data_validade().year + 4)
        self.cod_seguranca = '{}{}{}'.format(random.randint(0,9), random.randint(0,9), random.randint(0,9))
        self.limite = 500
        self.conta_corrente = conta_corrente
        self._senha = '1234'
        
        conta_corrente.cartoes.append(self)
        
    
    @property 
    def senha(self):  
        return self._senha
        
        
    @senha.setter
    def senha(self, valor:str):
        
        if len(valor) == 4 and valor.isnumeric():
            print("Nova senha alterada")
            self._senha = valor
        else:
            print('Nova senha invalida')
    
    
    
    @staticmethod
    def _data_validade():
        fuso_horario = pytz.timezone('Brazil/West')
        horario = datetime.now(fuso_horario)
        return horario
    
    
    def _numero_gerador(self):
        random.randint(1000000000000000, 9999999999999999)

   
 

    