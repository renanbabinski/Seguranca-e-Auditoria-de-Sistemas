from operator import itemgetter


LETRAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#plain text de entrada
print("\nDigite o nome do arquivo legivel, em texto claro")
print("O ARQUIVO DEVE SE ENCONTRAR DENTRO NA PASTA  'plain_text' E POSSUIR EXTENSÃO '.txt' ")
arquivo = open('./plain_text/{}'.format(input()), 'r')
plain_text = arquivo.read()
arquivo.close()

#texto cifrado de entrada
print("\nDigite o nome do arquivo criptografado")
print("O ARQUIVO DEVE SE ENCONTRAR DENTRO NA PASTA  'cypher_text' E POSSUIR EXTENSÃO '.txt' ")
arquivo = open('./cypher_text/{}'.format(input()), 'r')
cypher_text = arquivo.read()
arquivo.close()

base_key = {}

for i, j in zip(plain_text, cypher_text):
    if i not in base_key and i.upper() in LETRAS:
        base_key.update({i:j})


print("CHAVE ENCONTRADA")


for item in sorted(base_key, key = itemgetter(0)):
    print("ORIGINAL: {}  =>  {} :CIFRADO".format(item, base_key[item]))


print("CHAVE:")
for item in sorted(base_key, key = itemgetter(0)):
    print("{}".format(base_key[item]).upper(), end='')