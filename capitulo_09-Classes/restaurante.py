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

    9.4 – Pessoas atendidas: Comece com seu programa do Exercício 9.1
    (página 225). Acrescente um atributo chamado number_served cujo
    valor default é 0.
    Crie uma instância chamada restaurant a partir dessa classe.
    Apresente o número de clientes atendidos pelo restaurante e, em 
    seguida, mude esse valor e exiba-o novamente.
    Adicione um método chamado set_number_served() que permita definir o
    número de clientes atendidos. Chame esse método com um novo número e
    mostre o valor novamente.
    Acrescente um método chamado increment_number_served() que permita
    incrementar o número de clientes servidos. Chame esse método com
    qualquer número que você quiser e que represente quantos clientes
    foram atendidos, por exemplo, em um dia de funcionamento.

HISTÓRICO
    20201111: João Paulo, novembro de 2020.
        - 9.1 – Restaurante (pg 204).

    20201311: João Paulo, novembro de 2020.
        - 9.4 – Pessoas atendidas (pg 210).

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

restaurante = Restaurant('alcazar', 'tradicional')

restaurante.describe_restaurant()
restaurante.open_restaurant()

print("\n9.4 – Pessoas atendidas: ")
restaurant = Restaurant('bom boi', 'churrascaria')
restaurant.describe_restaurant()
#restaurant.number_served = 42
#restaurant.numero_clientes()
#restaurant.number_served = 13
#restaurant.numero_clientes()

restaurant.set_number_served(42)
restaurant.numero_clientes()

restaurant.set_number_served(13)
restaurant.numero_clientes()

restaurant.increment_number_served(42)
