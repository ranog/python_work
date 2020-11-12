#! /usr/bin/env python3

"""
NOME
    tres_restaurantes.py - FAÇA VOÇE MESMO.

SINOPSES
    chmod +x tres_restaurauits.py
    ./tres_restaurantes.py

    Restaurante: Alcazar;
    Tipo de cozinha:  Tradicional.

    Restaurante: Vivá;
    Tipo de cozinha:  Gastronomia Variada.

    Restaurante: Bom Boi;
    Tipo de cozinha:  Churrascaria.

DESCRIÇÃO
    9.2 – Três restaurantes: Comece com a classe do Exercício 9.1. Crie
    três instâncias diferentes da classe e chame describe_restaurant()
    para cada instância.

HISTÓRICO
    20201211: João Paulo, novembro de 2020.
        - 9.2 – Três restaurantes (pg 204).

"""


class Restaurant():
    """Modela um restaurante"""

    def __init__(self, restaurant_name, cuisine_type):
        """Inicializa os atributos restaurant_name e cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        """Descreve o restaurante"""
        print("\nRestaurante: " + self.restaurant_name.title() + ";")
        print("Tipo de cozinha:  " + self.cuisine_type.title() + ".")


restaurante = Restaurant('alcazar', 'tradicional')
restaurante.describe_restaurant()

restaurante = Restaurant('vivá', 'gastronomia variada')
restaurante.describe_restaurant()

restaurante = Restaurant('bom boi', 'churrascaria')
restaurante.describe_restaurant()
