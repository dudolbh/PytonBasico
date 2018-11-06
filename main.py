#importação de classe espeficivas
from veiculo import Veiculo
from carro import Carro

caminhao1 = Veiculo('verde','ford',6,51)
print(caminhao1)
print(type(caminhao1))

print('Cor:',caminhao1.cor)
print('Marca:',caminhao1.marca)
print('Rodas:', caminhao1.rodas)
print('Tanque:', caminhao1.tanque)

caminhao2 = Carro('azul','fiat',42)

print('Cor:',caminhao2.cor)
print('Marca:',caminhao2.marca)
print('Rodas:', caminhao2.rodas)
print('Tanque:', caminhao2.tanque)

caminhao2.abastecer(10)
print('Capacidade Tanque:', caminhao2.tanque)


caminhao1.abastecer(105)
print('Capacidade Tanque:', caminhao1.tanque)
