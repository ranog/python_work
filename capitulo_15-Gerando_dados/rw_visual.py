#!/usr/bin/env python3

"""
HISTÓRICO
    20211003: João Paulo, março de 2021.
        - Gerando vários passeios aleatórios (pg 379-380).
"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Indice para o salvamento automatico:
i = 0

# Continua criando novos passeios enquanto o programa estiver ativo:
while True:
    # Cria um passeio aleatório e plota os pontos:
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15) 

    # Salva os gráficos automaautomatic:
    plt.savefig('random_walk_plot' + str(i) + '.png')
    i += 1
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
