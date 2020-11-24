#! /usr/bin/env python3

"""
NOME
    gatos_e_cachorros.py - Gatos e cachorros.

SINOPSES
    chmod +x gatos_e_cachorros.py
    ./gatos_e_cachorros.py

------------------------------------------------------------------------

DESCRIÇÃO
    10.8 – Gatos e cachorros:
        Crie dois arquivos, cats.txt e dogs.txt. Armazene pelo menos
        três nomes de gatos no primeiro arquivo e três nomes de cachorro
        no segundo arquivo. Escreva um programa que tente ler esses
        arquivos e mostre o conteúdo do arquivo na tela. Coloque seu
        código em um bloco try-except para capturar o erro FileNotFound
        e apresente uma mensagem simpática caso o arquivo não esteja
        presente. Mova um dos arquivos para um local diferente de seu
        sistema e garanta que o código no bloco except seja executado de
        forma apropriada.

------------------------------------------------------------------------

HISTÓRICO
    20202411: João Paulo, novembro de 2020.
        - 10.8 - Gatos e cachorros (pg 248).

"""


def ler_arquivo(arquivos):
    """Abre um arquivo e devolve uma lista do conteudo."""

    try:
        with open(arquivos) as objeto:
            conteudo = objeto.read()

    except FileNotFoundError:
        print("Desculpa mas o arquivo " +
               arquivos +
               " não está em casa nesse momento, somente depois das 18:00 horas.")

    else:
        print("Nomes para seu animal de estimação:\n " + str(conteudo))


nomes_animais = ['cats.txt', 'dogs.txt']

for nome_animal in nomes_animais:
    ler_arquivo(nome_animal)
