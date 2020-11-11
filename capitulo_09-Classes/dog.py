#! /usr/bin/env python3

"""
NOME
    dog.py - Criando a classe Dog.

SINOPSES


DESCRIÇÃO
    Definimos uma classe chamada Dog. Por convenção, nomes com a
    primeira letra maiúscula referem-se a classes em Python. Os
    parênteses na definição da classe estão vazios porque estamos
    criando essa classe do zero.
    Escrevemos uma docstring que descreve o que essa classe faz.

    - Método __init__()

    Uma função que faz parte de uma classe é um método. Tudo que
    aprendemos sobre funções também se aplica aos métodos.
    
HISTÓRICO
    20201011: João Paulo, novembro de 2020.
        - Criando a classe Dog (pg 200-202).

"""


class Dog():
    """Uma tentativa simples de modelar um cachorro."""


    def __init__(self, name, age):
        """Inicializa os atributos name e age."""
        self.name = name
        self.age = age


    def sit(self):
        """Simula um cachorro sentando em resposta a um comando."""
        print(self.name.title() + " is now sitting.")


    def roll_over(self):
        """Simula um cachorro rolando em resposta a um comando."""
        print(self.name.title() + " rolled over!")
