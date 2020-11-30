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


class AnonymousSurvey():
    """Coleta respostas anônimas para uma pergunta de uma pesquisa."""


    def __init__(self, question):
        """Armazena uma pergunta e se prepara para armazenar as
        respostas."""
        self.question = question
        self.responses = []


    def show_question(self):
        """Mostra a pergunta da pesquisa."""
        print(self.question)


    def store_response(self, new_response):
        """Armazena uma única resposta da pesquisa."""
        self.responses.append(new_response)


    def show_results(self):
        """Mostra todas as respostas dadas."""
        print("Survey results: ")
        for response in self.responses:
            print("- " + response)
