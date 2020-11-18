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
    - ('Ignora as diferenças entre letras maiúsculas e minúsculas ao
    verificar a igualdade.',)

    lista comprehension:
    - Uma list comprehension combina o laço for e a criação de novos
    elementos em uma linha, e concatena cada novo elemento
    automaticamente (Ex: squares = [value**2 for value in range(1,11)])..

    [:]:
    - Para copiar uma lista, podemos criar uma fatia que inclua a lista
    original inteira omitindo o primeiro e o segundo índices ([:]). Isso
    diz a Python para criar uma lista que começa no primeiro item e
    termina no último, gerando uma cópia da lista toda.

    title():
    - Exibe cada palavra com uma letra maiúscula no início.

    upper():
    - Pode mudar uma string para que tenha somente letras  maiúsculas.

    rstrip():
    - Garante que não haja espaços em branco do lado direito de uma
    string.

    str():
    - Essa função diz a Python para representar valores que não  são
    strings como strings.

    sorted():
    - Permite exibir sua lista em uma ordem em particular, mas não afeta
    a ordem propriamente dita da lista.

DESCRIÇÃO
    9.13 – Reescrevendo o programa com OrderedDict: Comece com o
    Exercício 6.4 (página 155), em que usamos um dicionário-padrão para
    representar um glossário. Reescreva o programa usando a classe
    OrderedDict e certifique-se de que a ordem da saída coincida com a
    ordem em que os pares chave-valor foram adicionados ao dicionário.

------------------------------------------------------------------------

HISTÓRICO
    20201811: João Paulo, novembro de 2020
        - 9.13 – Reescrevendo o programa com OrderedDict (pg 225).

"""


from collections import OrderedDict


glossario = OrderedDict()

glossario['range'] = 'Facilita gerar uma série de números.'
glossario['len'] = 'Retorna o tamanho de uma lista em Python.'
glossario['lower'] = 'Ignora as diferenças entre letras maiúsculas e minúsculas ao verificar a igualdade.',
glossario['comprehension'] = 'Uma list comprehension combina o laço for e a \
criação de novos elementos em uma linha, e concatena cada novo elemento\
 automaticamente (Ex: squares = [value**2 for value in range(1,11)])..'
glossario['[:]'] = 'Para copiar uma lista, podemos criar uma fatia que inclua \
a lista original inteira omitindo o primeiro e o segundo índices ([:]). Isso \
diz a Python para criar uma lista que começa no primeiro item e termina no \
último, gerando uma cópia da lista toda.'
glossario['title'] = 'Exibe cada palavra com uma letra maiúscula no início.'
glossario['upper'] = 'Pode mudar uma string para que tenha somente letras  maiúsculas.'
glossario['rstrip'] = 'Garante que não haja espaços em branco do lado direito de uma string.'
glossario['str'] = 'Essa função diz a Python para representar valores que não \
são strings como strings.'
glossario['sorted'] = 'Permite exibir sua lista em uma ordem em particular, mas não afeta a ordem propriamente dita da lista.'

for word, meaning in glossario.items():
    if word == '[:]':
        print(word + ":\n- " + meaning + "\n")
    elif word == 'comprehension':
        print("lista " + word + ":\n- " + meaning + "\n")
    else:
        print(word + "():\n- " +str(meaning) + "\n")
