#Classe Cliente
class Cliente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
#muda o print padrão
    def __str__(self):
        return 'Cliente: '+self.nome+'\nCPF: '+self.cpf +'\nIdade: '+str(self.idade)
