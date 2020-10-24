#! /usr/bin/env python3

"""
NOME
    glossario.py - FAÇA VOCÊ MESMO

SINOPSES
    chmod +x glossario.py
    ./glossario.py

    range():
    - Facilita gerar uma série de números.

    len():
    - Retorna o tamanho de uma lista em Python.

    lower():
    - Ignora as diferenças entre letras maiúsculas e minúsculas ao
    verificar a igualdade.

    lista comprehension:
    - Uma list comprehension combina o laço for e a criação de novos
    elementosem uma linha, e concatena cada novo elemento
    automaticamente (Ex: squares = [value**2 for value in range(1,11)]).

    [:]:
    - Para copiar uma lista, podemos criar uma fatia que inclua a lista
    original inteira omitindo o primeiro e o segundo índices ( [:] ).
    Isso diz a Python para criar uma lista que começa no primeiro item e
    termina no último, gerando uma cópia da lista toda.

DESCRIÇÃO
    - 6.3 – Glossário:

    Um dicionário Python pode ser usado para modelar um dicionário de
    verdade. No entanto, para evitar confusão, vamos chamá-lo de
    glossário.

    • Pense em cinco palavras relacionadas à programação que você
    conheceu nos capítulos anteriores. Use essas palavras como chaves em
    seu glossário e armazene seus significados como valores.

    • Mostre cada palavra e seu significado em uma saída formatada de
    modo elegante. Você pode exibir a palavra seguida de dois-pontos e
    depois o seu significado, ou apresentar a palavra em uma linha e
    então exibir seu significado indentado em uma segunda linha. Utilize
    o caractere de quebra de linha (\n) para inserir uma linha em branco
    entre cada par palavra- significado em sua saída.

----------------------------------------------------------------------

HISTÓRICO
    20202410: João Paulo, outubro de 2020.
        - FAÇA VOCÊ MESMO 6.3 - Glossário - Pag. 138.

"""


glossario = {
    'range' : 'Facilita gerar uma série de números.',

    'len' : 'Retorna o tamanho de uma lista em Python.',

    'lower' : 'Ignora as diferenças entre letras maiúsculas e minúsculas ao\
 verificar a igualdade.',

    'comprehension' : 'Uma list comprehension combina o laço for e a criação de\
 novos elementos em uma linha, e concatena cada novo elemento automaticamente\
 (Ex: squares = [value**2 for value in range(1,11)]).',

    '[:]' : 'Para copiar uma lista, podemos criar uma fatia que inclua a lista\
 original inteira omitindo o primeiro e o segundo índices ( [:] ). Isso diz a\
 Python para criar uma lista que começa no primeiro item e termina no último,\
 gerando uma cópia da lista toda.',}

print("\nrange():\n- " + glossario['range'] +
      "\n\nlen():\n- " + glossario['len'] +
      "\n\nlower():\n- " + glossario['lower'] +
      "\n\nlista comprehension:\n- " + glossario['comprehension'] +
      "\n\n[:]:\n- " + glossario['[:]'])
