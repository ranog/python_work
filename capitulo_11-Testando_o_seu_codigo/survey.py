#! /usr/bin/env python3

"""
------------------------------------------------------------------------

NOME
    survey.py - Uma classe para testar.

------------------------------------------------------------------------
SINOPSES
    from survey import AnonymousSurvey

------------------------------------------------------------------------

DESCRIÇÃO
    - Uma classe para testar:
        Essa classe começa com uma pergunta fornecida por você para uma
        pesquisa e inclui uma lista vazia para armazenar as respostas. A
        classe tem métodos para exibir a pergunta da pesquisa, adicionar
        uma nova resposta à lista de respostas e exibir todas as
        respostas armazenadas na lista. Para criar uma instância dessa
        classe, tudo que precisamos fazer é fornecer uma pergunta.
        Depois de ter criado uma instância que represente uma pesquisa
        em particular, você mostrará a pergunta da pesquisa com
        show_question(), armazenará uma resposta com store_response() e
        exibirá o resultado com show_results().

        Essa classe funciona para uma pesquisa anônima simples.

------------------------------------------------------------------------

HISTÓRICO
    20202811: João Paulo, novembro de 2020.
        - Uma classe para testar (pg 265-266).

    20202911: João Paulo, novembro de 2020.
        - Continuação: Uma classe para testar (pg 265-266).

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
