#! /usr/bin/env python3

"""
NOME
    palavras_comuns.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x palavras_comuns.py
    ./palavras_comuns.py

    - A quantidade de vezes que a palavra 'the' aparece em 'arquivos/The
    Project Gutenberg eBook of The Anglers Of Arz, by Roger Dee..html' é
    de 488 vezes.

    - A quantidade de vezes que a palavra 'the' aparece em 'arquivos/The
    Project Gutenberg eBook of Assignment's End, by Roger Dee..html' é
    de 772 vezes.

    - A quantidade de vezes que a palavra 'the' aparece em 'arquivos/The
    Project Gutenberg E-text of Chivalry, by James Branch Cabell.html' é
    de 4378 vezes.

------------------------------------------------------------------------

DESCRIÇÃO
    10.10 – Palavras comuns:
        Acesse o Projeto Gutenberg (http://gutenberg.org/ ) e encontre
        alguns textos que você gostaria de analisar. Faça download dos
        arquivos-texto dessas obras ou copie o texto puro de seu
        navegador para um arquivo-texto em seu computador. Você pode
        usar o método count() para descobrir quantas vezes uma palavra
        ou expressão aparece em uma string. Por exemplo, o código a
        seguir conta quantas vezes a palavra 'row' aparece em uma
        string:
            >>> line = 'Row, row, row your boat'
            >>> line.count('row')
            2
            >>> line.lower().count('row')
            3

        Observe que converter a string para letras minúsculas usando
        lower() faz com que todas as formas da palavra que você está
        procurando sejam capturadas, independentemente do modo como elas
        estiverem grafadas. Escreva um programa que leia os arquivos que
        você encontrou no Projeto Gutenberg e determine quantas vezes a
        palavra 'the' aparece em cada texto.

------------------------------------------------------------------------

HISTÓRICO
    20202411: João Paulo, novembro de 2020.
        - 10.10 – Palavras comuns (pg 249).
"""


def ler_aquivos(arquivos, palavra):
    """Lê arquivos e determine quantas vezes uma palavra aparece em
       cada texto.
    """

    with open(arquivos) as objeto:
        conteudo = objeto.read()

    print("\n- A quantidade de vezes que a palavra '" +
           palavra + "' aparece em '" +
           arquivo + "' é de " + str(conteudo.lower().count(palavra)) +
           " vezes.")

palavra = 'the'
arquivos = ['arquivos/The Project Gutenberg eBook of The Anglers Of Arz, by Roger Dee..html',
            'arquivos/The Project Gutenberg eBook of Assignment\'s End, by Roger Dee..html',
            'arquivos/The Project Gutenberg E-text of Chivalry, by James Branch Cabell.html']

for arquivo in arquivos:
    ler_aquivos(arquivo, palavra)
