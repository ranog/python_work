#! /usr/bin/env python3

"""
NOME
    restaurant.py - FAÇA VOÇE MESMO.

SINOPSES
    import restaurant
    nome_do_objeto = nome_do_módulo.nome_da_classe()

DESCRIÇÃO
    9.10 – Importando Restaurant: Usando sua classe Restaurant mais
    recente, armazene-a em um módulo. Crie um arquivo separado que
    importe Restaurant.
    Crie uma instância de Restaurant e chame um de seus métodos para
    mostrar que a instrução import funciona de forma apropriada.

HISTÓRICO
    20201711: João Paulo, novembro de 2020.
        - 9.4 – Importando Restaurant (pg 223-224).

"""


class Restaurant():
    """Modela um restaurante"""

    def __init__(self, restaurant_name, cuisine_type):
        """Inicializa os atributos restaurant_name e cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """Descreve o restaurante"""
        print("\nRestaurante: " + self.restaurant_name.title() +
              "\nCulinária: " + self.cuisine_type.title())


    def open_restaurant(self):
        """Horário de funcionamento do restaurante"""
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
