lista_nomes = ['João','Maria','Guilherme','Diego']
#for identifuca automaticamente a quantidade de itens na lista
for nome in lista_nomes:
    print(nome)

lista_numeros = range(0,100,2)

'''for num in lista_numeros:
    print(num)
'''
#outra forma de utilizar o for
for i in range(len(lista_nomes)):
    print(lista_nomes[i])
#stringe tbm é considerada uma coleção
palavra = 'Eduardo Barros'
for i in palavra:
    print(i)

#while
i=0
while i < 10:
    print('i ainda é menor que 10: ',i)
    i = i + 1
    #i +=1 outra forma de incrementar

print('Acabou o while')


#interomper um while
numero = 0
while True:
    if numero == 20:
        break
    print(numero)
    numero +=1