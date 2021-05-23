# Cifra Simples de Substituição

import random, sys

LETRAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def menu_modo():
    escolha = int(input("DIGITE O MODO DESEJADO: \n (1) Criptografar \n (2) Descriptografar\n"))
    if escolha == 1:
        print("MODO :  CRIPTOGRAFAR")
        return 'criptografar'
    else:
        print("MODO :  DESCRIPTOGRAFAR")
        return 'descriptografar'
    

def chave_valida(chave):
    lista_chaves = list(chave)
    lista_letras = list(LETRAS)
    lista_chaves.sort()
    lista_letras.sort()

    return lista_letras == lista_chaves


def criptografar_mensagem(chave, mensagem):
    return traduzir_mensagem(chave, mensagem, 'criptografar')


def descriptografar_mensagem(chave, mensagem):
    return traduzir_mensagem(chave, mensagem, 'descriptografar')


def traduzir_mensagem(chave, mensagem, modo):
    traducao = ''
    alfabetoA = LETRAS
    alfabetoB = chave
    if modo == 'descriptografar':
        alfabetoA, alfabetoB = alfabetoB, alfabetoA
    for simbolo in mensagem:
        if simbolo.upper() in alfabetoA:
            indice_simbolo = alfabetoA.find(simbolo.upper())
            if simbolo.isupper():
                traducao += alfabetoB[indice_simbolo].upper()
            else:
                traducao += alfabetoB[indice_simbolo].lower()
        else:
            traducao += simbolo
    
    return traducao


def chave_aleatória():
    chave = list(LETRAS)
    random.shuffle(chave)
    return ''.join(chave)


def menu_chave(modo):
    if modo == 'criptografar':
        escolha = int(input("ESCOLHA UMA OPÇÃO:\n 1)Digitar uma chave manual\n 2)Gerar chave aleatória\n"))
        if escolha == 1:
            chave = input("Digite sua chave:")
            if chave_valida(chave):
                return chave
            else:
                sys.exit("A chave digitada é inválida!")
        else:
            chave = chave_aleatória()
            print("CHAVE ALEATÓRIA GERADA:  {}".format(chave))
            return chave
    else:
        chave = input("Digite sua chave:")
        if chave_valida(chave):
            return chave
        else:
            sys.exit("A chave digitada é inválida!")
1



######################################################################

def main():
    
    

    modo = menu_modo()
    minha_chave = menu_chave(modo)

    if modo == 'criptografar':
        print("\nDigite o nome do arquivo que deseja criptografar")
        print("O ARQUIVO DEVE SE ENCONTRAR DENTRO NA PASTA  'plain_text' E POSSUIR EXTENSÃO '.txt' ")
        arquivo = open('./plain_text/{}'.format(input()), 'r')
        minha_mensagem = arquivo.read()
        arquivo.close()
        traducao = criptografar_mensagem(minha_chave, minha_mensagem)
    elif modo == 'descriptografar':
        print("\nDigite o nome do arquivo que deseja descriptografar")
        print("O ARQUIVO DEVE SE ENCONTRAR DENTRO NA PASTA  'cypher_text' E POSSUIR EXTENSÃO '.txt' ")
        arquivo = open('./cypher_text/{}'.format(input()), 'r')
        minha_mensagem = arquivo.read()
        arquivo.close()
        traducao = descriptografar_mensagem(minha_chave, minha_mensagem)
    
    print("Usando a chave {}".format(minha_chave))
    print("Ao {}, o resultado foi:\n\n ".format(modo))
    print(traducao)


    arquivo = open('./saida/{}'.format(input("\n\nDigite o nome para o arquivo de saída:")), 'w')
    arquivo.write(traducao)
    arquivo.close()

if __name__ == '__main__':
    main()