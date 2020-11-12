#! /usr/bin/env python3

"""
NOME
    restaurante.py - FAÇA VOÇE MESMO.

SINOPSES
    chmod +x restaurante.py
    ./restaurante.py

    O Alcazar tem uma culinária tradicional.
    - Horário de funcionamento:
            06:00-11:00
            11:30-23:00

DESCRIÇÃO
    9.1 – Restaurante: Crie uma classe chamada Restaurant.
    O método __init__() de Restaurant deve armazenar dois atributos:
    restaurant_name e cuisine_type. Crie um método chamado
    describe_restaurant() que mostre essas duas informações, e um
    método de nome open_restaurant() que exiba uma mensagem informando
    que o restaurante está aberto.
    Crie uma instância chamada restaurant a partir de sua classe. Mostre
    os dois atributos individualmente e, em seguida, chame os dois
    métodos.
    
    acesso ao site (11 de novembro de 2020):
        https://www.google.com/amp/s/viagemeturismo.abril.com.br/
        especiais/os-restaurantes-mais-classicos-de-sao-paulo-por
        -especialidade/amp/

HISTÓRICO
    20201111: João Paulo, novembro de 2020.
        - 9.1 – Restaurante (pg 204).

"""


class Restaurant():
    """Modela um restaurante"""

    def __init__(self, restaurant_name, cuisine_type):
        """Inicializa os atributos restaurant_name e cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Descreve o restaurante"""
        print("\nO " + self.restaurant_name.title() +
              " tem uma culinária " + self.cuisine_type + ".")

    def open_restaurant(self):
        """Horário de funcionamento do restaurante"""
        print("- Horário de funcionamento:\n\t06:00-11:00\n\t11:30-23:00") 

restaurante = Restaurant('alcazar', 'tradicional')

restaurante.describe_restaurant()
restaurante.open_restaurant()
