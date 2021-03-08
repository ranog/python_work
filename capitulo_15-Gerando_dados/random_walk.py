#!/usr/bin/env python3

"""
HISTÓRICO
    20210803: João Paulo, março de 2021.
        - Criando a classe RandomWalk() (pg 377).
"""

from random import choice


class RandomWalk():
    """
        Uma classe para gerar passeios aleatórios.
    """

    def __init__(self, num_points=5000):
        """
            Inicializa os atributos de um passeio.
        """
        self.num_points = num_points
        
        # Todos os passeios começam em (0, 0):
        self.x_values = [0]
        self.y_values = [0]
