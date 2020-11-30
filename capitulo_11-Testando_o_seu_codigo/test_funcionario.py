#! /usr/bin/env python3

"""
------------------------------------------------------------------------

NOME
    test_funcionario.py - FAÇA VOCÉ MESMO.

------------------------------------------------------------------------

SINOPSES
    $ chmod +x test_funcionario .py
    $ ./test_funcionario.py
    18500
    .15000
    .
    --------------------------------------------------------------------
    Ran 2 tests in 0.001s

    OK

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
        teste, test_give_default_raise() e test_give_custom_raise().
        Use o método setUp() para que não seja necessário criar uma nova
        instância de funcionário em cada método de teste. Execute seu
        caso de teste e certifique-se de que os dois testes passem.

------------------------------------------------------------------------

HISTÓRICO
    20203011: João Paulo, novembro de 2020.
        - 11.3 – Funcionário (pg 270).

------------------------------------------------------------------------
"""


import unittest
from funcionario import Employee


class TestEmployee(unittest.TestCase):
    """Testes para a classe A Employee."""


    def setUp(self):
        """Cria uma funcionario que podera ser usados em todos os
        métodos de teste."""
        nome = "Eric"
        sobrenome = "Cire"
        salario_anual = 10000
        self.funcionario = Employee(nome, sobrenome, salario_anual)


    def test_give_default_raise(self):
        """Testa o valor de aumento padrão."""
        salario = self.funcionario.give_raise()
        self.assertEqual(self.funcionario.salario_anual, 15000)


    def test_give_custom_raise(self):
        """Testa o valor de aumento customizado."""
        salario = self.funcionario.give_raise(8500)
        self.assertEqual(self.funcionario.salario_anual, 18500)


unittest.main()
