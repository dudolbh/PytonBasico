'''
Exercicio:
Faça um programa que pergunte a idade, o peso e a altura de uma pessoa e decide se ela está aapta a ser do exercito
Para entrar no exercito é preciso ter mais de 18 anos pesar mais de 60 kilos e mefir mais de 1,70 metros
'''
idade = input('Informe a idade:')
peso = input('Informe o peso:')
altura = input('Informe a altura:')

#Valid exercito
if int(idade) > 18 and int(peso) > 60 and float(altura) > 1.70:
    print('Apto a entrar no exercito')
else:
    print('Não está apto a entrar no exercito')