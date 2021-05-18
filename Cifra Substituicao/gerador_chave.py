import random
from datetime import datetime

# O alfabeto inglês e português possuem a mesma quantidade de letras, 26
# Vamos adicionar também o espaço ' ', o ponto '.', e a virgula ',', totalizando 27

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','.',',']

#print(len(alfabeto))
#print(alfabeto)
#Mostra tamanho e composição do alfabeto original

random.shuffle(alfabeto) #aleatoriza as posições da lista

#print(len(alfabeto))
#print(alfabeto)
#Mostra tamanho e composição do alfabeto aleatório
print("#######       CHAVE GERADA     #########")

#Gera arquivo com timestamp e escreve nele o alfabeto aleatório
arquivo = open('./chaves_geradas/key_'+str(datetime.timestamp(datetime.now()))+'.txt', 'w')
for i in alfabeto:
    arquivo.write(str(i))
    print(str(i),end=" ")

arquivo.close()
