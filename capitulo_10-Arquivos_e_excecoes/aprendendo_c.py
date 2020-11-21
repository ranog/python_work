#! /usr/bin/env python3

"""
NOME
    aprendendo_c.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x aprendendo_c.py
    ./aprendendo_c.py
    Em C podemos representar um string colando-o entre aspas ou
    apóstrofes.
    Em C podemos colocar um else no laço de repetição e que será
    executado no final da iteração.
    Em C podemos usar variáveis também para armazenar e processar
    textos.
    Em C podemos ter listas de números, strings e também de valores
    booleanos.
    Em C podemos usar and para exigir que duas condições sejam
    verdadeiras ao mesmo tempo.
    Em C podemos usar o método findall() para extrair todas as
    substrings que correspondem à expressão regular.
    Em C podemos usar uma estrutura while ou uma estrutura for.
    Em C podemos implementar e definir a funcionalidade de diversos
    operadores como +, *,. == como parte de nossas classes.


------------------------------------------------------------------------

DESCRIÇÃO
    10.2 – Aprendendo C: Você pode usar o método replace() para
    substituir qualquer palavra por uma palavra diferente em uma string.
    Eis um exemplo rápido que mostra como substituir a palavra 'dog' por
    'cat' em uma frase:

    >>> message = 'I really like dogs.'
    >>> message.replace('dog', 'cat') 'I really like cats.'

    Leia cada linha do arquivo learning_python.txt que você acabou de
    criar e substitua a palavra Python pelo nome de outra linguagem, por
    exemplo, C.
    Mostre cada linha modificada na tela.

------------------------------------------------------------------------

HISTÓRICO
    20202011: João Paulo, novembro de 2020.
        - 10.2 – Aprendendo C (pg 237).

"""


filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

learning_string = ''

for line in lines:
    learning_string += line.replace('Python', 'C')

print(learning_string.strip())
