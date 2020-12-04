#! /usr/bin/env python3

"""
------------------------------------------------------------------------

NOME
    bar_descriptions.py - Acrescentando dicas de contexto
    personalizadas.

------------------------------------------------------------------------

SINOPSES
    $ chmod +x bar_descriptions.py
    $ ./bar_descriptions.py

------------------------------------------------------------------------

DESCRIÇÃO
    Definimos uma lista chamada plot_dicts, que contém três dicionários:
    um para o projeto HTTPie, um para o projeto Django e outro para o
    Flask.
    Cada dicionário tem duas chaves: 'value' e 'label'. O Pygal usa o
    número associado a 'value' para descobrir a altura que cada barra
    deve ter, e utiliza a string associada a 'label' para criar a dica
    de contexto de cada barra. Por exemplo, o primeiro dicionário criará
    uma barra que representa um projeto com 16.101 estrelas, e sua dica
    de contexto conterá Description of httpie (Descrição de httpie).
    O método add() precisa de uma string e de uma lista. Quando chamamos
    esse método, passamos a lista de dicionários que representa as
    barras (plot_dicts).
    O Pygal inclui o número de estrelas como uma dica de contexto
    default, além da dica de contexto personalizada que lhe passamos.

------------------------------------------------------------------------

HISTÓRICO
    20200412: João Paulo, dezembro de 2020.
        - Acrescentando dicas de contexto personalizadas (pg 434).

------------------------------------------------------------------------
"""


import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


my_style = LS('#333366', base_style=LCS)

chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [{'value' : 16101, 'label' : 'Description of httpie.'},
        {'value' : 15028, 'label' : 'Description of django.'},
        {'value' : 14798, 'label' : 'Description of flask.'}, ]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')
