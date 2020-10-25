#! /usr/bin/env python3

"""
NOME
    glossario.py - FAÇA VOCÊ MESMO

SINOPSES
    chmod +x glossario.py
    ./glossario.py
    [:]:
    - Para copiar uma lista, podemos criar uma fatia que inclua a lista
    original inteira omitindo o primeiro e o segundo índices ( [:] ).
    Isso diz a Python para criar uma lista que começa no primeiro item e
    termina no último, gerando uma cópia da lista toda.

    lista comprehension:
    - Uma list comprehension combina o laço for e a criação de novos
    elementos em uma linha, e concatena cada novo elemento
    automaticamente (Ex: squares = [value**2 for value in range(1,11)]).

    len():
    - Retorna o tamanho de uma lista em Python.

    lower():
    - Ignora as diferenças entre letras maiúsculas e minúsculas ao
    verificar a igualdade.

    range():
    - Facilita gerar uma série de números.

    rstrip():
    - Garante que não haja espaços em branco do lado direito de uma
    string.

    sorted():
    - Permite exibir sua lista em uma ordem em particular, mas não afeta
    a ordem propriamente dita da lista.

    str():
    - Essa função diz a Python para representar valores que não são
    strings como strings.

    title():
    - Exibe cada palavra com uma letra maiúscula no início.

    upper():
    - Pode mudar uma string para que tenha somente letras maiúsculas.


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

    - 6.4 – Glossário 2:

    Agora que você já sabe como percorrer um dicionário com um laço,
    limpe o código do Exercício 6.3 (página 148), substituindo sua
    sequência de instruções print por um laço que percorra as chaves e
    os valores do dicionário. Quando tiver certeza de que seu laço
    funciona, acrescente mais cinco termos de Python ao seu glossário.
    Ao executar seu programa novamente, essas palavras e significados
    novos deverão ser automaticamente incluídos na saída.

------------------------------------------------------------------------

HISTÓRICO
    20202410: João Paulo, outubro de 2020.
        - FAÇA VOCÊ MESMO 6.3 - Glossário - Pag. 138.

    20202510: João Paulo, outubro de 2020
        - FAÇA VOCÊ MESMO 6.4 - Glossário 2 (pg 143).

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
 gerando uma cópia da lista toda.',

    'title' : 'Exibe cada palavra com uma letra maiúscula no início.',

    'upper' : 'Pode mudar uma string para que tenha somente letras\
 maiúsculas.',

    'rstrip' : 'Garante que não haja espaços em branco do lado direito\
 de uma string.',

    'str' : 'Essa função diz a Python para representar valores que não\
 são strings como strings.',

    'sorted' : 'Permite exibir sua lista em uma ordem em particular,\
 mas não afeta a ordem propriamente dita da lista.',}

"""
print("\nrange():\n- " + glossario['range'] +
      "\n\nlen():\n- " + glossario['len'] +
      "\n\nlower():\n- " + glossario['lower'] +
      "\n\nlista comprehension:\n- " + glossario['comprehension'] +
      "\n\n[:]:\n- " + glossario['[:]'])
"""

for word, meaning in sorted(glossario.items()):
    if word == '[:]':
        print(word + ":\n- " + meaning + "\n")
    elif word == 'comprehension':
        print("lista " + word + ":\n- " + meaning + "\n")
    else:
        print(word + "():\n- " + meaning + "\n")
