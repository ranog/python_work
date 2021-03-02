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


    O parâmetro linewidth controla a espessura da linha gerada por
    plot().

    A função title() define um título para o gráfico.

    Os parâmetros fontsize, que aparecem repetidamente pelo código,
    controlam o tamanho do texto no gráfico.

    As funções xlabel() e ylabel() permitem definir um título para cada
    um dos eixos, e a função tick_params() estiliza as marcações nos
    eixos x.

    Os argumentos mostrados aqui afetam as marcações tanto no eixo x
    quanto no eixo y (axes='both') e definem o tamanho da fonte dos
    rótulos das marcações com 14 ( labelsize=14 ).

------------------------------------------------------------------------

HISTÓRICO
    20202412: João Paulo, dezembro de 2020.
        - Gerando um gráfico linear simples (pg 369).

    20212802: João Paulo, fevereiro de 2021.
        - Alterando o tipo do rótulo e a espessura do gráfico
        (pg 369-370).

    20210203: João Paulo, março de 2021.
        - Corrigindo o gráfico (pg 371).

------------------------------------------------------------------------
"""


import matplotlib.pyplot as plt


input_valeus = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.plot(input_valeus, squares, linewidth=5)

# Define o título do gráfico e nomeia os eixos.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Define o tamanho dos rótulos das marcações.
plt.tick_params(axis='both', labelsize=14)
plt.show()
