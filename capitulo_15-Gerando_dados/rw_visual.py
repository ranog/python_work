#!/usr/bin/env python3

"""
HISTÓRICO
    20211003: João Paulo, março de 2021.
        - Gerando vários passeios aleatórios (pg 379-380).

    20211203: João Paulo, março de 2021.
        - Plotando os pontos de início e de fim (pg 381-382).

    20211303: João Paulo, março de 2021.
        - Limpando os eixos (pg 382).

    20211403: João Paulo, março de 2021.
        - Adicionando pontos para plotagem (pg 382-383);
        - Alterando o tamanho para preencher a tela (pg 383-384).
"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Indice para o salvamento automatico:
i = 0

# Continua criando novos passeios enquanto o programa estiver ativo:
while True:
    # Cria um passeio aleatório:
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Define o tamanho da janela de plotagem:
    plt.figure(figsize=(16, 9))


    # Plota os pontos e mostra o gráfico:
    point_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
            edgecolor='none', s=1)

    # Enfatiza o primeiro e o último ponto:
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
            s=100)

    # Remove os eixos:
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    # Salva os gráficos automaautomatic:
    plt.savefig('random_walk_plot_sem_eixos' + str(i) + '.png')
    i += 1

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
