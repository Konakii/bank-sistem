class Pessoa:
    def __init__(self,nome,idade,rg):
        self.nome = nome
        self.idade = idade
        self.rg = rg
        
class Cliente(Pessoa):
    def __init__(self, nome, idade, rg,conta):
        super().__init__(nome, idade, rg)
        self.conta = conta
    
    def autenticar(self,rg):
        if rg == self.rg:
            print('você está autenticado')
            return
        print("usuario inválido")

cliente1 = Cliente('jardel',18,181818,'bradesco')

cliente1.autenticar(181818)
