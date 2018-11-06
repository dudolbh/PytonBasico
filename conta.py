#classe conta
class Conta:
    def __init__(self,cliente,saldo,limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite

    def __str__(self):
        return 'Cliente: '+ self.cliente.nome +'\nSaldo: ' + str(self.saldo) + '\nSaldo + Limite: ' + str(self.saldo+self.limite)

    def saque(self,valor):
        if self.saldo - valor < self.limite*-1:
            print("Saldo insuficiente")
        else: self.saldo -= valor

    def deposito(self,valor):
        self.saldo += valor