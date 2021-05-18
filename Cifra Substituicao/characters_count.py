arquivo = open('./textos_normais/large.txt','r')

texto = arquivo.readlines()

texto = str(texto)

print(texto)

characters_found = {}

for i in texto:
    #print(i)
    if i not in characters_found and i != '[' and i != ']' and i != "'":
        characters_found.update({i: texto.count(str(i))})

for caracter, quantidade in characters_found.items():
    print('Key:',caracter, 'Quantidade:',quantidade)

