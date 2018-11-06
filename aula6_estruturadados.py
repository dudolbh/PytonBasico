minha_lista = ['Gui','Joao'] #Lista (Lista) - Ordenado
minha_tupla = ('Gui','Joao') #TUPLA (tuple) - É imutavel não permite adicionar e remover objetos
meu_dicionario = {'nome': 'Eduardo','idade':31}# Dicionario (dict) Tabela HASH Chave(Key) e Valor(value)
meu_conjunto ={'Eduardo','Isabela','Gui'} #CONJUNTO (Set) Não permite valor dulicado e não é ordenado, não tem indice.

#prguntar se um item está na lista, tupla, conjunto
if 'Gui' in minha_lista:
    print('Gui esta na lista')
else: print('Gui não está na lista')

#Trabalhar com o dicionario
print(meu_dicionario['nome'])
if 'Eduardo' in meu_dicionario.values():
    print('Eduardo esta no dicionario')
else: print('Eduardo não está na dicionario')
#Adicionar itens no dicionario
meu_dicionario['endereco'] = 'Rua Francisco'
print(meu_dicionario)

#Conjunto e dicionario a busca é instantanea
meu_conjunto.add('Leo')
print(meu_conjunto)

#incializaçao de estruturas vazias
lista = []
tupla = ()
dicionario = {}
conjunto = set()
