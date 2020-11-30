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
    ..
    --------------------------------------------------------------------
    Ran 2 tests in 0.001s

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


    - Método setUp():
        O método setUp() faz duas tarefas: cria uma instância da
        pesquisa e cria uma lista de respostas. Cada um desses dados é
        prefixado com self para que possam ser usados em qualquer lugar
        na classe. Isso simplifica os dois métodos de teste, pois nenhum
        deles precisará criar uma instância da pesquisa ou uma resposta.
        O método test_store_single_response() verifica se a primeira
        resposta em self.responses – self.responses[0] – pode ser
        armazenada corretamente, e test_store_single_response() verifica
        se todas as três respostas em self.responses podem ser
        armazenadas corretamente. Quando executamos test_survey.py de
        novo, vemos que os dois testes continuam passando. Esses testes
        seriam particularmente úteis se tentássemos expandir
        AnonymousSurvey de modo a tratar várias respostas para cada
        pessoa. Depois de modificar o código para que aceite várias
        respostas, você poderia executar esses testes e garantir que não
        afetou a capacidade de armazenar uma única resposta ou uma série
        de respostas individuais.
        
        Quando testar suas próprias classes, o método setUp() poderá
        facilitar a escrita de seus métodos de teste. Crie apenas um
        conjunto de instâncias e de atributos em setUp() e então utilize
        essas instâncias em todos os seus métodos de teste. Isso é muito
        mais fácil que criar um novo conjunto de instâncias e de
        atributos em cada método de teste.


    - NOTA:
        Durante a execução de um caso de teste, Python exibe um
        caractere para cada teste de unidade à medida que ele terminar.
        Um teste que passar exibe um ponto, um teste que resulte em erro
        exibe um E e um teste que resultar em uma asserção com falha
        exibe um F. É por isso que você verá um número diferente de
        pontos e de caracteres na primeira linha da saída quando
        executar seus casos de teste. Se um caso de teste demorar muito
        para executar por conter muitos testes de unidade, você poderá
        observar esses resultados para ter uma noção de quantos testes
        estão passando.

------------------------------------------------------------------------

HISTÓRICO
    20202911: João Paulo, novembro de 2020.
        - Testando a classe AnonymousSurvey (pg 267-268).
        - Método setUp() (pg 268-270).

------------------------------------------------------------------------

"""


import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Testes para a classe AnonymousSurvey."""


    def setUp(self):
        """Cria uma pesquisa e um conjunto de respostas que poderão ser
        usados em todos os métodos de teste."""
        question = "What language did you first learn to speak? "
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']


    def test_store_single_response(self):
        """Testa se uma única resposta é armazenada de forma
        apropriada."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)


    def test_store_three_responses(self):
        """Testa se três respostas individuais são armazenadas de forma
        apropriada."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()
