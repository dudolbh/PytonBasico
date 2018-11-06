# \\ para caractere scape
# open com r é leitura read, w gravação read. r+ escrita e leitura, metodo a apend.
# arquivos diferentes de txt deve ser aberto com r/w b - binario
arquivo= open('arquivo.txt','w')
#arquivo.write('Teste gravação arquivo')

for i in range(1,1001):
    arquivo.write('aaaaa '+str(i)+ '\n')