#! /usr/bin/env python3

"""
NOME
    lista_de_convidado.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x lista_de_convidado.py
    ./lista_de_convidado.py

    Digitando 'quit' o programa é encerrado.
    Seu nome, por favor: johnny
    Johnny obrigado por usar nossos programas.

    Digitando 'quit' o programa é encerrado.
    Seu nome, por favor: quit

------------------------------------------------------------------------

DESCRIÇÃO
    10.4 – Lista de convidados: Escreva um laço while que pergunte o
    nome aos usuários. Quando fornecerem seus nomes, apresente uma
    saudação na tela e acrescente uma linha que registre a visita do
    usuário em um arquivo chamado guest_book.txt. Certifique-se de que
    cada entrada esteja em uma nova linha do arquivo.

------------------------------------------------------------------------

HISTÓRICO
    20202111: João Paulo, novembro de 2020.
        - 10.4 - Lista de convidado (pg 240).

"""


filename = 'guest_book.txt'

while True:
    print("\nDigitando 'quit' o programa é encerrado.")
    username = input("Seu nome, por favor: ")

    if username.lower() != 'quit':
        print(username.title() + " obrigado por usar nossos programas.")

        with open(filename, 'a') as file_object:
            file_object.write(username.lower() + "\n")

    else:
        break
