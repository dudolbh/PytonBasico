print('Hello World! \nSegundo Print')
#nome = 'Eduardo'
#idade = 31
#altura = 1.85

nome = input('Escreva seu nome: ')
idade = input('Escreva seu idade: ')
altura = input('Escreva seu altura: ')

#tipo variaveis
tipo_nome = (type(nome))
tipo_idade = (type(idade))
tipo_altura = (type(idade))

frase = nome +' tem ' +str(idade) +' anos e ' + str(altura) + ' de altura.'

#saida
print(nome, 'tem',idade,'anos e',altura, 'de altura.')
print(frase)

#Numero elevado
numero1 = 2**2
print('2 elevado 2=',numero1)
#Raiz quadrada
numero2 = 4**(1/2)
print ('raiz quadrada 4=', numero2)