# Comparadores: == != > < >= <=
var_verdadeiro = False
var_falso = False

print(type(var_verdadeiro),type(var_falso))

if var_verdadeiro == True:
    print('var_verdade é verdadeiro')
else:
    print('var_verdade é falsa')


##Exercicio
print('Menu:\n1 = Galo\n2 = Cruzeiro\n3 = America')
opcao = input('Escolha a opção:')
#elif utilizado como um case, qualquer condição atentidad sai do programa
#not utilizado para negar a afirmação
if opcao == '1':
    print('Galo.')
elif opcao == '2':
    print('Marias.')
elif opcao =='3':
    print('Cuei.')
else:
    print('Opção inválida.')

if not True:
    print('Entrou no if')
else:
    print('Entrou no else')