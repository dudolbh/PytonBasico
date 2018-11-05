frase = 'Oi, tudo bem?'
print(frase[0])

lista_nomes = ['João','Maria','Guilherme','Diego']
print(lista_nomes)
print(lista_nomes[0:3])
#pular caracteres
print(frase[0:12:2])
#ultimo valor da lista
print(frase[-1])
#lista de tras para frente
print(lista_nomes[-1:-5:-1])
#inverter a lista
print(frase[::-1])

#incluir itens na lista
lista_nomes.append('Eduardo')
print(lista_nomes)
#remover itens da lista
lista_nomes.remove('João')
print(lista_nomes)
#Inserindo itens em indices especificos
lista_nomes.insert(1,'Patrick')
print(lista_nomes)
#update no indices
lista_nomes[0] = 'Update'
print(lista_nomes)

#contragem de registros na lista
contador = lista_nomes.count('Eduardo')
#tamanho da lista
tamanho = len(lista_nomes)
print(contador, tamanho)
#pop retira da lista na ordem de inserção


#separar strings split.
frase_separada = frase.split(',')
print(frase_separada)