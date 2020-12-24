#! /usr/bin/env python3

"""
------------------------------------------------------------------------

NOME
    mpl_squares.py - Gerando um gráfico linear simples.

------------------------------------------------------------------------

SINOPSES
    $ chmod +x mpl_squares.py
    $ ./mpl_squares.py

------------------------------------------------------------------------

DESCRIÇÃO
    Inicialmente importamos pyplot usando o alias plt para que não seja
    necessário digitar pyplot repetidamente. (Você verá essa convenção
    com frequência em exemplos online, portanto faremos o mesmo aqui.)

    O módulo pyplot contém várias funções que ajudam a gerar gráficos e
    plotagens.

    Criamos uma lista para armazenar os quadrados e então a passamos
    para a função plot(), que tentará plotar os números de forma
    significativa.

    plt.show() abre o visualizador do matplotlib e exibe o gráfico.

    O visualizador permite fazer zoom e navegar pelo gráfico; se você
    clicar no ícone do disco, poderá salvar a imagem de qualquer gráfico
    que quiser.

------------------------------------------------------------------------

HISTÓRICO
    20202412: João Paulo, dezembro de 2020.
        - Gerando um gráfico linear simples (pg 369).

------------------------------------------------------------------------
"""


import matplotlib.pyplot as plt


squares = [1, 4, 9, 16, 25]

plt.plot(squares)
plt.show()
