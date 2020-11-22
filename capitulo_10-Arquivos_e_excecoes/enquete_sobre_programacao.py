#! /usr/bin/env python3

"""
NOME
    enquete_sobre_programacao.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x enquete_sobre_programacao.py
    ./enquete_sobre_programacao.py

    Digitando 'quit' o programa é encerrado.
    Por que você gosta de programação: Programação é arte
    Obrigado por sua resposta.

    Digitando 'quit' o programa é encerrado.
    Por que você gosta de programação: Programar é trabalhar em equipe
    Obrigado por sua resposta.

    Digitando 'quit' o programa é encerrado.
    Por que você gosta de programação: Programar é fazer a diferença na
    vida das pessoas
    Obrigado por sua resposta.

    Digitando 'quit' o programa é encerrado.
    Por que você gosta de programação: Programar é inventar coisas novas
    Obrigado por sua resposta.

    Digitando 'quit' o programa é encerrado.
    Por que você gosta de programação: Programar é resolver problemas
    Obrigado por sua resposta.

    Digitando 'quit' o programa é encerrado.
    Por que você gosta de programação: Programação é a combinação
    perfeita entre criatividade e matemática
    Obrigado por sua resposta.

    Digitando 'quit' o programa é encerrado.
    Por que você gosta de programação: Programar é divertido
    Obrigado por sua resposta.

    Digitando 'quit' o programa é encerrado.
    Por que você gosta de programação: quit

------------------------------------------------------------------------

DESCRIÇÃO
    10.5 – Enquete sobre programação: Escreva um laço while que pergunte
    às pessoas por que elas gostam de programação. Sempre que alguém
    fornecer um motivo, acrescente-o em um arquivo que armazene todas as
    respostas.

------------------------------------------------------------------------

HISTÓRICO
    20202111: João Paulo, novembro de 2020.
        - 10.5 - Enquete sobre programação (pg 240).

"""


filename = 'todas_as_respostas.txt'

while True:
    print("\nDigitando 'quit' o programa é encerrado.")
    resposta = input("Por que você gosta de programação: ")

    if resposta.lower() != 'quit':
        print("Obrigado por sua resposta.")

        with open(filename, 'a') as file_object:
            file_object.write(resposta.lower() + "\n")

    else:
        break
