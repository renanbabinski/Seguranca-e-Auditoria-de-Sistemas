import pprint


def gera_padrao_palavra(palavra):
    # Retorna uma string no formato do padrao da palavra
    # Exemplo  '0.1.2.3.4.1.2.3.5.6' para 'DUSTBUSTER'
    palavra = palavra.upper()
    proximo_numero = 0
    numero_letras = {}
    padrao_palavra = []

    for letra in palavra:
        if letra not in numero_letras:
            numero_letras[letra] = str(proximo_numero)
            proximo_numero += 1
        padrao_palavra.append(numero_letras[letra])
    return '.'.join(padrao_palavra)


def main():
    todos_padroes = {}

    arquivo = open('./dicionario_ingles/dictionary.txt')
    lista_palavras = arquivo.read().split('\n')
    arquivo.close()

    for palavra in lista_palavras:
        # Gerar o padrão de cada palavra ma lista de palavras
        padrao = gera_padrao_palavra(palavra)

        if padrao not in todos_padroes:
            todos_padroes[padrao] = [palavra]
        else:
            todos_padroes[padrao].append(palavra)

    # Este código gera outro código. O arquivo padrao_palavras.py contém
    # todos os padrões de todas as palavras do dicionário

    arquivo = open('padrao_palavras.py', 'w')
    arquivo.write('todos_padroes = ')
    arquivo.write(pprint.pformat(todos_padroes))
    arquivo.close()


if __name__ == '__main__':
    main()