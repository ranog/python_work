#!/usr/bin/env python3

"""
FAÇA VOCÊ MESMO
    15.1 – Cubos: Um número elevado à terceira potência é chamado de
    cubo. Faça a plotagem dos cinco primeiros números elevados ao cubo
    e, em seguida, dos primeiros 5.000 números elevados ao cubo.

    15.2 – Cubos coloridos: Aplique um colormap ao seu gráfico de cubos.
"""

import matplotlib.pyplot as plt

x_values = list(range(1, 6)) # 5 primeiros números
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens,
        edgecolor='none', s=40)

# Define o título do gráfico e nomeia os eixos.
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

# Define o intervalor para os 5 primeiros números:
plt.axis([0, 10, 0, 150])

# Salva o gráfico dos 5 primeiros números automaticamente:
plt.savefig('cube_first_five_numbers_plot.png')


# Define o valor de x_values para os primeiros 5.000 números elevados
# ao cubo:
X_values = list(range(1,5001))
Y_values = [X**3 for X in X_values]

plt.scatter(X_values, Y_values, c=Y_values, cmap=plt.cm.Reds,
        edgecolor='none', s=40)

plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

# Define o intervalor para os 5 primeiros números:
plt.axis([0, 5100, 0, 150000000000])

# Salva o gráfico dos 5 primeiros números automaticamente:
plt.savefig('cube_first_five_thousand_numbers_plot.png')
