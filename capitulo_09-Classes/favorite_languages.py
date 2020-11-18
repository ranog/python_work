#! /usr/bin/env python3

"""
NOME
    favorite_languages.py - Biblioteca-padrão de Python.

SINOPSES
    chmod +x favorite_languages.py
    ./favorite_languages.py
    Jen's favorite language is Python.
    Sarah's favorite language is C.
    Edward's favorite language is Ruby.
    Phil's favorite language is Pytiuui

DESCRIÇÃO
    Começamos importando a classe OrderedDict do módulo collections.
    Criamos uma instância da classe OrderedDict e a armazenamos em
    favorite_languages. Observe que não há chaves; a chamada a
    OrderedDict() cria um dicionário ordenado vazio para nós e o
    armazena em favorite_languages. Então adicionamos cada nome
    linguagem em favorite_languages, um de cada vez. Agora, quando
    percorremos favorite_languages com um laço, sabemos que sempre
    teremos as respostas na ordem em que os itens foram adicionados.

------------------------------------------------------------------------

HISTÓRICO
    20201811: João Paulo, outubro de 2020.
        - Biblioteca-padrão de Python (pg 224-225).

"""


from collections import OrderedDict


favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
