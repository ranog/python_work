#!/usr/bin/env python3

"""
HISTÓRICO
    20211003: João Paulo, março de 2021.
        15.3 – Movimento molecular: Modifique rw_visual.py substituindo
        plt.scatter() por plt.plot(). Para simular o percurso de um grão
        de pólen na superfície de uma gota d’água, passe rw.x_values e
        rw.y_values e inclua um argumento linewidth. Utilize 5.000 em
        vez de 50.000 pontos.
"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Indice para o salvamento automatico:
i = 0

# Continua criando novos passeios enquanto o programa estiver ativo:
while True:
    # Cria um passeio aleatório:
    rw = RandomWalk()
    rw.fill_walk()

    # Define o tamanho da janela de plotagem:
    plt.figure(figsize=(16, 9))


    # Plota os pontos e mostra o gráfico:
    point_numbers = list(range(rw.num_points))

    plt.plot(rw.x_values, rw.y_values, c=point_numbers, linewidth=5)

    # Enfatiza o primeiro e o último ponto:
    plt.plot(0, 0, c='green')
    plt.plot(rw.x_values[-1], rw.y_values[-1], c='red')

    # Remove os eixos:
#    plt.axes().get_xaxis().set_visible(False)
#    plt.axes().get_yaxis().set_visible(False)

    # Salva os gráficos automaticamente:
#    plt.savefig('movimento_molecular.png')
#    i += 3

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
      break
