#!/usr/bin/env python3

"""
HISTÓRICO
    20211003: João Paulo, março de 2021.
        - Gerando vários passeios aleatórios (pg 379-380).
"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk


# Continua criando novos passeios enquanto o programa estiver ativo:
while True:
    # Cria um passeio aleatório e plota os pontos:
    rw = RandomWalk()
    rw.fill_walk()

    plt.scatter(rw.x_values, rw.y_values, s=15) 

    # Salva o gráfico automaticamente:      
    plt.savefig('random_walk_plot.png')

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
