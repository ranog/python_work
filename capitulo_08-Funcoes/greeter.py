#! /usr/bin/env python3

"""
NOME
    greeter.py - Definindo uma função.

SINOPSES
    chmod +x greeter.py
    ./greeter.py

    Hello!

DESCRIÇÃO
    Esse exemplo mostra a estrutura mais simples possível para uma
    função. A palavra reservada def para informa Python que estamos
    definindo uma função. Essa é a definição da função, que informa o
    nome da função a Python e, se for aplicável, quais são os tipos de
    informação necessários à função para que ela faça sua tarefa. Os
    parênteses contêm essa informação. Nesse caso, o nome da função é
    greet_user(), e ela não precisa de nenhuma informação para executar
    sua tarefa, portanto os parênteses estão vazios. (Mesmo assim, eles
    são obrigatórios.) Por fim, a definição termina com dois-pontos.

    Qualquer linha indentada após def greet_user(): faz parte do corpo
    da função. O texto entre aspas é um comentário chamado
    docstring, que descreve o que a função faz. As docstrings são
    colocadas entre aspas triplas, que Python procura quando gera a
    documentação das funções de seus programas.

    A linha print("Hello!") é a única linha com código propriamente dito
    no corpo dessa função, portanto greet_user() realiza apenas uma
    tarefa: print("Hello!").

    Quando quiser usar essa função, você deve chamá-la. Uma chamada de
    função diz a Python para executar o código da função. Para chamar
    uma função, escreva o nome dela, seguido de qualquer informação
    necessária entre parênteses. Como nenhuma informação é necessária
    nesse caso, chamar nossa função é simples e basta fornecer
    greet_user().

HISTÓRICO
    20200111: João Paulo, outubro de 2020.
        - Definindo uma função (pg 169).

"""


def greet_user():
    print("\nHello!")

greet_user()
