#! /usr/bin/env python3

"""
------------------------------------------------------------------------

NOME
    funcionario.py - FAÇA VOCÊ MESMO.

------------------------------------------------------------------------

SINOPSES

------------------------------------------------------------------------

DESCRIÇÃO
    11.3 – Funcionário:
        Escreva uma classe chamada Employee. O método __init__() deve
        aceitar um primeiro nome, um sobrenome e um salário anual, e
        deve armazenar cada uma dessas informações como atributos.
        Escreva um método de nome give_raise() que some cinco mil
        dólares ao salário anual, por default, mas que também aceite um
        valor diferente de aumento.
        Escreva um caso de teste para Employee. Crie dois métodos de
        teste, test_give_default_raise() e test_give_custom_raise(). Use
        o método setUp() para que não seja necessário criar uma nova
        instância de funcionário em cada método de teste. Execute seu
        caso de teste e certifique-se de que os dois testes passem.

------------------------------------------------------------------------

HISTÓRICO
    20203011: João Paulo, novembro de 2020.
        - 11.3 – Funcionário (pg 270).

------------------------------------------------------------------------

"""


class Employee():
    """Modelo simples de um funcionario e seus ganhos anuais."""


    def __init__(self, nome, sobrenome, salario_anual):
        """Inicialização dos atributos do funcionario."""
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario_anual = salario_anual


    def give_raise(self, aumento=5000):
        """Soma cinco mil dólares ao salário anual."""
        
        plus = input("Aumento padrão de $5.000, (S)im ou (n)ão? ")

        if plus.lower() == 's':
            self.salario_anual += aumento
            print(self.salario_anual)
        else:
            aumento = input("Novo valor: ")
            aumento = float(aumento)
            self.salario_anual += aumento
            print(self.salario_anual)
