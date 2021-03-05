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

    20210503: João Paulo, março de 2021.
        - Calculando dados automaticamente (pg 373-374);
        - Removendo os contornos dos pontos de dados (pg 374).
"""

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, edgecolor='none', s=40)

# Define o título do gráfico e nomeia os eixos:
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Define o tamanho dos rótulos das marcações:
plt.tick_params(axis='both', which='major', labelsize=14)

# Define o intervalo para cada eixo:
plt.axis([0, 1100, 0, 1100000])

plt.show()
