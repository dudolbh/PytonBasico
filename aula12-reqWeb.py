import requests
#get, busca requisisão
#post, aplica a solitação
#Status 200 requsição ok

s = requests.Session()

try:
    requsicao = requests.get('http://google.com')
except Exception as e:
    print('Erro:',e)

print(requsicao.text) #ver o conteudo