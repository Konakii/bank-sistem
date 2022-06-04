from pessoa_banco import Cliente

from abc import ABC, abstractmethod

class SI(ABC,Cliente):
    def __init__(self,banco,saldo,nome,idade,rg,conta):
        super().__init__(nome, idade, rg, conta)
        self._banco = banco
        self._saldo = saldo
        

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self,valor):
        if not isinstance(valor,(int,float)):
            raise ValueError('Saldo precisa ser numérico!')
        self._saldo = valor

    
    def depositar(self,valor):
        self.valor = valor
        if not isinstance:
            raise ValueError('Deposito precisa ser numérico!')
        self.saldo += valor
        print(f'você depositou {self.valor}')
        
    def sacar(self,valor):
        self.valor = valor
        if self._saldo < self.valor:
            print('você não pode sacar oque não tem!')
            return
        
        self.saldo -= valor
        print(f'você sacou {self.valor}')
