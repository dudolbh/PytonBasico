try:
    a=1200 / 0
#identificadno o erro
except Exception as erro:
    print('Aconteceu um erro:',erro)
print('aaaaaa')

#utilizar exeption para abertura de conexão, leitura de arquvos etc.
'''
except ZeroDivisionError:
    print('Divisão por Zero')
except NameError:
    print('Você digirou o valor errado')
'''

#time.sleep dorme a aplicação