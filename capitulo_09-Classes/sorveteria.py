#! /usr/bin/env python3

"""
NOME
    sorveteria.py - FAÇA VOÇE MESMO.

SINOPSES
    chmod +x sorveteria.py
    ./sorveteria.py

    Restaurante: Giolitti
    Culinária: Sorveteria Tradicional
    Flavors:
    - Nozes
    - Pistache
    - Frutas Vermelhas

DESCRIÇÃO
    9.6 – Sorveteria: Uma sorveteria é um tipo específico de
    restaurante. Escreva uma classe chamada IceCreamStand que herde da
    classe Restaurant escrita no Exercício 9.1 (página 225) ou no
    Exercício 9.4 (página 232). Qualquer versão da classe funcionará;
    basta escolher aquela de que você mais gosta.
    Adicione um atributo chamado flavors que armazene uma lista de
    sabores de sorvete. Escreva um método para mostrar esses sabores.
    Crie uma instância de IceCreamStand e chame esse método.

HISTÓRICO
    20201511: João Paulo, novembro de 2020.
        - 9.6 – Soreveteria (pg 217).

"""


class Restaurant():
    """Modela um restaurante"""

    def __init__(self, restaurant_name, cuisine_type):
        """Inicializa os atributos restaurant_name e cuisine_type.
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """Descreve o restaurante.
        """
        print("\nRestaurante: " + self.restaurant_name.title() +
              "\nCulinária: " + self.cuisine_type.title())


    def open_restaurant(self):
        """Horário de funcionamento do restaurante.
        """
        print("- Horário de funcionamento:\n\t06:00-11:00\n\t11:30-23:00")


    def numero_clientes(self):
        """Apresenta o número de clientes atendidos pelo restaurante.
        """
        print("- Foram atendidos " + str(self.number_served) + " clientes.")


    def set_number_served(self, clientes):
        """Permite definir o número de clientes atendidos
        """
        if clientes >= 0:
            self.number_served = clientes


    def increment_number_served(self, cliente):
        """Incrementa o número de clientes servidos.
        """
        self.number_served += cliente
        print("- Atendemos " + str(self.number_served) +
              " clientes em um dia de funcionamento.")


class IceCreamStand(Restaurant):
    """Modelo simplificado de uma sorveteria.
    """
    def __init__(self, restaurant_name, cuisine_type):
        """Inicializa os atributos da classe-pai (Restaurant).
        E inicializa uma lista de sabores de sorvete (self.flavors).
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []


    def flavor(self):
        """Armazena uma lista de sabores de sorvete e mostra esses
        sabores.
        """
        self.flavors = ['nozes', 'pistache', 'frutas vermelhas']

        print("Flavors: ")

        for self_flavor in self.flavors:
            print("- " + self_flavor.title())


sorveteria = IceCreamStand('giolitti', 'sorveteria tradicional')
sorveteria.describe_restaurant()
sorveteria.flavor()
