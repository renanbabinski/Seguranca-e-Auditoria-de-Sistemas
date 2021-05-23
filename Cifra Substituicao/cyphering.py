

#plain text de entrada
plain_text_txt = open('./textos_normais/large.txt', 'r')
plain_text = plain_text_txt.read()

#chave de criptografia
key_txt = open('./chaves_geradas/minha_chave.txt', 'r')
key = key_txt.readline()

#texto cifrado de saída
cypher_text_txt = open('./textos_cifrados/large_cypher.txt', 'w')

#alfabeto base
alfabeto_txt = open('./chaves_geradas/alfabeto_base.txt', 'r')
alfabeto = alfabeto_txt.readline()

print("KEY:  {}".format(key))
print("ALFABETO:   {}".format(alfabeto))

print("Prévia da substituição:  LETRA => CHAVE")

for (i, j) in zip(alfabeto, key):
    print('{} => {}'.format(i, j))

for i in plain_text:
    index = alfabeto.index(i)
    cypher_text_txt.write(key[index])