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
"""

import matplotlib.pyplot as plt

plt.scatter(2, 4, s=200)

# Define o título do gráfico e nomeia os eixos.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Define o tamanho dos rótulos das marcações.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
