#importando bibliotecas
import sys
argumentos = sys.argv #Arg 1 - Tipo , Arg 2 - Numero 1, Arg 3 Numero 2

def soma(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

retorno = 0
if argumentos[1] == 'soma':
    retorno = soma(float(argumentos[2]),float(argumentos[3]))
elif argumentos[2] == 'sub':
    retorno = sub(float(argumentos[2]),float(argumentos[3]))

print(retorno)