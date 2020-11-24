#! /usr/bin/env python3

"""
NOME
    sum.py - FAÇA VOCÊ MESNO.

SINOPSES
    chmod +x sum.py
    ./sum.py


------------------------------------------------------------------------

DESCRIÇÃO
    10.6 – Adição: Um problema comum quando pedir entradas numéricas
        ocorre quando as pessoas fornecem texto no lugar de números. Ao
        tentar converter a entrada para um int, você obterá um
        TypeError.
        Escreva um programa que peça dois números ao usuário. Some-os e
        mostre o resultado. Capture o TypeError caso algum dos valores
        de entrada não seja um número e apresente uma mensagem de erro
        simpática. Teste seu programa fornecendo dois números e, em
        seguida, digite um texto no lugar de um número.

------------------------------------------------------------------------

HISTÓRICO
    20202411: João Paulo, novembro de 2020.
        - 10.6 - Adição (pg 248).

"""


def soma(x, y):
    """Soma dois números"""
    try:
        z = float(x) + float(y)
    
    except:
        print("- Não podemos realizar essa soma no momento, volte mais tarde. ;)")

    else:
        print(str(x) + " + " + str(y) + " = " + str(z))

while True:
    print("\n- Entre com 'q' para sair.")
    x = input("Entre com o 1° número: ")
    if x.lower() == 'q':
        break

    y = input("Entre com o 2° número: ")
    if y.lower() == 'q':
        break

