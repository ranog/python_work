"""
HOSTÓRICO
    20211703: João Paulo, março de 2021.
        Criando a classe Die (pg 385-386).
"""

from random import randint


class Die():
    """
        Uma classe que representa um único dado.
    """


    def __init__(self, num_sides=6):
        """
            Supõe que seja um dado de seis lados.
        """
        self.num_sides = num_sides


    def roll(self):
        """"
            Devolve um valor aleatório entre 1 e o número de lados.
        """
        return randint(1, self.num_sides)
