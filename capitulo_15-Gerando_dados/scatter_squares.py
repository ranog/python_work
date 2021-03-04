#!/usr/bin/env python3

"""
DESCRIÇÃO
    Chamamos scatter() e usamos o argumento s para definir o tamanho dos
    pontos usados para desenhar o gráfico. Ao executar
    scatter_squares.py agora, você deverá ver um único ponto no meio do
    gráfico.


HISTÓRICO
    20210303: João Paulo, março de 2021.
        - Plotando e estilizando pontos individuais com scatter()
        (pg 372).

    20210403: João Paulo, março de 2021.
        - Plotando uma série de pontos com scatter() (pg 373).
"""

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values, y_values, s=100)

# Define o título do gráfico e nomeia os eixos.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Define o tamanho dos rótulos das marcações.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
