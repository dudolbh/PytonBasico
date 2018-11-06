'''
Exercicio: Faça uma função que receba um objeto de coleção e retorne o maior valor
dentro dessa colecao
faca outra função que retorne o menor numero desta colecao
'''
# função maior valor
def max_value(lista):
    v_maior = lista[0]
    for i in lista:
        if int(i) > v_maior:
            v_maior = int(i)
    return v_maior

#funçao menor valor
def min_value(lista):
    v_menor = lista[0]
    for i in lista:
        if int(i) < v_menor:
            v_menor = int(i)
    return v_menor

#Inicialização lista
lista_num = []
for i in range(6):
    lista_num.append(i)
print(lista_num)

maiorvalor = max_value(lista_num)
print(maiorvalor)

menorvalor = min_value(lista_num)
print(menorvalor)