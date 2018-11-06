#definição da função
def soma(numero1,numero2):
    resp=numero1+numero2
    return resp

retorno= soma(2.2,4.4)
print(retorno)

#Varios retornos
def tem_sete_itens (var):
    if len(var) == 7:
        return True
    else: return False

frase= '1234567'#'Ola tudo bem?'
if tem_sete_itens(frase):
    print('Tem sete itens na lista')
else: print('Não tem 7 itens na lista')


#metodo geralmente não tem retorno, função passa o x e retorna o y