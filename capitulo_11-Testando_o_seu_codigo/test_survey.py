#! /usr/bin/env python3

"""
------------------------------------------------------------------------

NOME
    test_survey.py - Testando a classe AnonymousSurvey.

------------------------------------------------------------------------

SINOPSES
    $ chmod +x test_survey.py
    $ ./test_survey.py
    .
   ---------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK

------------------------------------------------------------------------
    ..
    --------------------------------------------------------------------
    Ran 2 tests in 0.000s

    OK

------------------------------------------------------------------------

DESCRIÇÃO
    - Testando a classe AnonymousSurvey:
        Começamos importando o módulo unittest e a classe que queremos
        testar, isto é, AnonymousSurvey. Chamamos nosso caso de teste de
        TestAnonymousSurvey que, novamente, herda de unittest.TestCase.
        O primeiro método de teste verificará se quando armazenamos uma
        resposta à pergunta da pesquisa, ela será inserida na lista de
        respostas da pesquisa. Um bom nome descritivo para esse método é
        test_store_single_response(). Se esse teste falhar, pelo nome do
        método mostrado na saída do teste que falhou saberemos que houve
        um problema na armazenagem de uma única resposta à pesquisa.
        Para testar o comportamento de uma classe, precisamos criar uma
        instância dessa classe. Criamos uma instância chamada my_survey
        com a pergunta "What language did you first learn to speak?" .
        Armazenamos uma única resposta, English , usando o método
        store_response() . Então conferimos se a resposta foi armazenada
        corretamente confirmando se English está na lista
        my_survey.responses

        Chamamos o novo método de test_store_three_responses(). Criamos
        um objeto para a pesquisa, exatamente como fizemos em
        test_store_single_response(). Definimos uma lista contendo três
        respostas diferentes e, então, chamamos store_response() para
        cada uma dessas respostas. Depois que as respostas foram
        armazenadas, escrevemos outro laço e conferimos se cada resposta
        está agora em my_survey.responses.

        Quando executamos test_survey.py novamente, vemos que os dois
        testes (para uma única resposta e para três respostas) passam.

------------------------------------------------------------------------

HISTÓRICO
    20202911: João Paulo, novembro de 2020.
        - Testando a classe AnonymousSurvey (pg 267-268).

------------------------------------------------------------------------

"""


import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Testes para a classe AnonymousSurvey."""


    def test_store_single_response(self):
        """Testa se uma única resposta é armazenada de forma
        apropriada."""
        question = "What language did you first learn to speak? "
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)


    def test_store_three_responses(self):
        """Testa se três respostas individuais são armazenadas de forma
        apropriada."""
        question = "What language did you first learn to spead? "
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)


unittest.main()
