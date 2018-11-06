'''Execicio: faça um programa que leia a quantidade de pessoas que serão
convidadas para uma festa.
Apos isso o programa ira perguntar o nome de todas as pessoas e colocar numa lista de convidados
Apos isso imprimir toda a lista
'''
qtd_convid = input('Informe a quantidade de convidados:')
lista_conv = []
i=1
while i <= int(qtd_convid):
    nome=input('Infome o nome do convidado '+str(i)+':')
    lista_conv.append(nome)
    i+=1

print('Lista de convidados\n', lista_conv)