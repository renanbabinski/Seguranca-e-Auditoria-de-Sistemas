#Hackeando a cifra de substituição com dicionários

import re
import gerar_padrao_palavras
import padrao_palavras
import cifra_sub_simples
import copy


LETRAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
somente_palavras =  re.compile('[^A-Z\s]')


def gerar_mapeamento_cifras_letras_vazio():
    # Retorna um dicionário vazio para mapeamento de letras criptografadas
     return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [],
           'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [],
           'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [],
           'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}

def adicionar_letras_ao_mapeamento(mapa_letras, palavra_cifrada, candidato):
    # O parâmetro mapa_letras recebe um dicionário que armazena o mapeamento das
    # palavras cifradas, que é copiado pela função.
    # O parâmetro palavra_cifrada é um valor string de uma palavra cifrada
    # O parâmetro candidato é uma possível palavra do Inglês que a palavra cifrada
    # pode ser descriptografada

    # Esta função adiciona as letras do candidato como potenciais letras
    # para a descriptografia, e adiciona essas letras no mapeamento

    for i in range(len(palavra_cifrada)):
        if candidato[i] not in mapa_letras[palavra_cifrada[i]]:
            mapa_letras[palavra_cifrada[i]].append(candidato[i])


def cruzar_mapeamentos(mapaA, mapaB):
    # Para cruzar dois mapas, crie um mapa em branco e então adicione a este mapa
    # somente as letras em potencial que existem em AMBOS os mapas

    mapa_interseccao = gerar_mapeamento_cifras_letras_vazio()
    
    for letra in LETRAS:
        # Uma lista vazia significa "qualquer letra possivel". Neste caso, copie o outro mapa
        # por inteiro:
        if mapaA[letra] == []:
            mapa_interseccao[letra] = copy.deepcopy(mapaB[letra])
        elif mapaB[letra] == []:
            mapa_interseccao[letra] = copy.deepcopy(mapaA[letra])
        else:
            # Se uma letra no mapaA[letra] existe no mapaB[letra],
            # adicione essa letra ao mapa de intersecção:
            for letra_mapeada in mapaA[letra]:
                if letra_mapeada in mapaB[letra]:
                    mapa_interseccao[letra].append(letra_mapeada)
        
    return mapa_interseccao


def remover_letras_resolvidas_do_mapeamento(mapa_letras):
    # Letras cifradas no mapeamento que apontam para apenas uma letra estão "resolvidas"
    # e podem ser removidas das outras letras
    # Por exemplo. se 'A' aponta para as potencias letras ['M', 'N'], e 'B'
    # aponta para ['N'], então nós sabemos que 'B' só aponta para 'N', então podemos remover 'N'
    # da lista em que 'A' aponta também. Agora 'A' irá apontar somente para 'M', então podemos remover 
    # 'M' dos outros mapeamentos e assim por diante
    # (Este é o motivo pelo qual esse loop permanece reduzindo o mapa)

    iterar_novamente = True
    while iterar_novamente:
        # Primeiro assumimos que não vamos iterar novamente:
        iterar_novamente = False

        # letras_resolvidas serão uma lista de letras maiusculas que tem um
        # e somente um mapeamento possivel no mapa_letras
        letras_resolvidas = []
        for letra_cifrada in LETRAS:
            if len(mapa_letras[letra_cifrada]) == 1:
                letras_resolvidas.append(mapa_letras[letra_cifrada][0])

        # Se uma letra está resolvida, então ela não pode ser uma potencial candidata
        # de outras letras cifradas, então devemos remove-las das outras listas:

        for letra_cifrada in LETRAS:
            for s in letras_resolvidas:
                if len(mapa_letras[letra_cifrada]) != 1 and s in mapa_letras[letra_cifrada]:
                    mapa_letras[letra_cifrada].remove(s)
                    if len(mapa_letras[letra_cifrada]) == 1:
                        # Uma nova letra foi resolvida, então itere novamente:
                        iterar_novamente = True
    
    return mapa_letras


def hack_cifra_simples_sub(mensagem):
    mapa_interseccao = gerar_mapeamento_cifras_letras_vazio()
    lista_palavras_cifradas = somente_palavras.sub('', mensagem.upper()).split()

    for palavra_cifrada in lista_palavras_cifradas:
        # gerar mapeamento de letras criptografadas vazio para cada palavra cifrada
        mapa_candidato = gerar_mapeamento_cifras_letras_vazio()

        padrao_palavra = gerar_padrao_palavras.gera_padrao_palavra(palavra_cifrada)

        if padrao_palavra not in padrao_palavras.todos_padroes:
            continue  #Esta palavra nao está no dicionário, então continue

        # Adicionar as letras de cada candidato ao mapeamento:
        for candidato in padrao_palavras.todos_padroes[padrao_palavra]:
            adicionar_letras_ao_mapeamento(mapa_candidato, palavra_cifrada, candidato)

        # Cruzar o novo mapeamento com o mapeamento existente:
        mapa_interseccao = cruzar_mapeamentos(mapa_interseccao, mapa_candidato)

    # Remova qualquer letras resolvidas de outras listas:
    return remover_letras_resolvidas_do_mapeamento(mapa_interseccao)


def descriptografar_cifra_com_mapeamento(texto_criptografado, mapa_letras):
    # Retorna uma string do texto descriptografado com o mapeamennto de letras,
    # qualquer letra ambigua (sem mapeamento único) é reposicionada com um
    # underscore "_"

    # Primeiro, crie uma sub-chave a partir do mapeamento:
    chave = ['x'] * len(LETRAS)
    for letra_cifrada in LETRAS:
        if len(mapa_letras[letra_cifrada]) == 1:
            # Se há somente uma letra mapeada, adicione a chave:
            index_chave = LETRAS.find(mapa_letras[letra_cifrada][0])
            chave[index_chave] = letra_cifrada
        else:
            texto_criptografado = texto_criptografado.replace(letra_cifrada.lower(), '_')
            texto_criptografado = texto_criptografado.replace(letra_cifrada.upper(), '_')
    chave = ''.join(chave)

    # Com a chave criada, descriptografe o texto:
    print("\nCHAVE DESCOBERTA:   {}\n".format(chave))
    return cifra_sub_simples.descriptografar_mensagem(chave, texto_criptografado)


def main():

    print("Digite o nome do arquivo que deseja descriptografar:")
    print("O ARQUIVO DEVE SE ENCONTRAR DENTRO DA PASTA 'cypher_text' E POSSUIR EXTENSÃO '.txt'")
    arquivo = open('./cypher_text/{}'.format(input()), 'r')
    mensagem = arquivo.read()
    arquivo.close()

    print("Hacking...")

    mapeamento_letras = hack_cifra_simples_sub(mensagem)

    # Mostrando os resultados ao usuário:
    print('Mapping:')
    print(mapeamento_letras)
    print()
    print("Texto criptografado original:")
    print(mensagem)
    print()
    mensagem_hackeada = descriptografar_cifra_com_mapeamento(mensagem, mapeamento_letras)
    print(mensagem_hackeada)
    print()


if __name__ == '__main__':
    main()