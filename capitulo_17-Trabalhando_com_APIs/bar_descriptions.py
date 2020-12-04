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
