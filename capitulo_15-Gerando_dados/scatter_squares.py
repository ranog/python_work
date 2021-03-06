#!/usr/bin/env python3

"""
DESCRIÇÃO
    Capítulo 15 Gerando dados.

HISTÓRICO
    20210303: João Paulo, março de 2021.
        - Plotando e estilizando pontos individuais com scatter()
        (pg 372).

    20210403: João Paulo, março de 2021.
        - Plotando uma série de pontos com scatter() (pg 373).

    20210503: João Paulo, março de 2021.
        - Calculando dados automaticamente (pg 373-374);
        - Removendo os contornos dos pontos de dados (pg 374).
        - Definindo cores personalizadas (pg 375).

    20210603: João Paulo, março de 2021.
        - Usando um colormap (pg 375-376);
        - Salvando seus gráficos automaticamente (pg 376).
"""

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

# Define o título do gráfico e nomeia os eixos:
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Define o tamanho dos rótulos das marcações:
plt.tick_params(axis='both', which='major', labelsize=14)

# Define o intervalo para cada eixo:
plt.axis([0, 1100, 0, 1100000])

# Salva o gráfico automaticamente:
plt.savefig('squares_plot.png')

# Remove espaços em branco extras do gráfico:
# plt.savefig('squares_plot.png', bbox_inches='tight')

# Exibe o gráfico:
plt.show()
