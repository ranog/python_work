#! /usr/bin/env python3

"""
NOME
    greeter.py - Definindo uma função.

SINOPSES
    chmod +x greeter.py
    ./greeter.py

    - Definindo uma função:
    Hello!

    - Passando informações para uma função:
    Hello, Jesse!
    Hello, Sarah!


DESCRIÇÃO
    - Definindo uma função:

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

    - Passando informações para uma função:

    Usar greet_users('jesse') faz greet_users() ser chamada e fornece as
    informações de que a função precisa para executar a instrução print.
    A função aceita o nome que você passar e exibe a saudação para esse
    nome.

    - Argumentos e parâmetros:

    Na função greet_users() anterior, definimos greet_users() para que
    exija um valor para a variável username. Depois que chamamos a
    função e lhe fornecemos a informação (o nome de uma pessoa), a
    saudação correta foi exibida.

    A variável username na definição de greet_users() é um exemplo de

        * parâmetro – uma informação de que a função precisa para
        executar sua tarefa.

    O valor 'jesse' em greet_users('jesse') é um exemplo de argumento.

        * argumento - uma informação passada para uma função em sua
        chamada.

    Quando chamamos a função, colocamos entre parênteses o valor com que
    queremos que a função trabalhe. Nesse caso, o argumento 'jesse' foi
    passado para a função greet_users() e o valor foi armazenado no
    parâmetro username.

HISTÓRICO
    20200211: João Paulo, outubro de 2020.
        - Definindo uma função (pg 169).
        - Passando informações para uma função (pg 170)

"""


def greet_user():
    print("Hello!")

def greet_users(username):
    """Exibe uma saudação simples."""
    print("Hello, " + username.title() + "!")

print("\n- Definindo uma função: ")
greet_user()

print("\n- Passando informações para uma função: ")
greet_users('jesse')
greet_users('sarah')
