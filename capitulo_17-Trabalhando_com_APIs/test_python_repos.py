#! /usr/bin/env python3

"""
NOME
    test_python_repos.py - FAÇA VOCÊ MESMO.

SINOPSES
    $ chmod +x test_python_repos.py
    $ ./test_python_repos.py
    ...
    --------------------------------------------------------------------
    Ran 3 tests in 2.641s

    OK
------------------------------------------------------------------------

DESCRIÇÃO
    17.3 – Testando python_repos.py: Em python_repos.py, exibimos o
    valor de status_code para garantir que a chamada de API foi
    bem-sucedida. Escreva um programa chamado test_python_repos.py que
    use unittest para conferir se o valor de status_code é 200. Descubra
    outras asserções que você possa fazer – por exemplo, se o número de
    itens devolvidos é o que se espera e se o número total de
    repositórios é maior que uma determinada quantidade.

------------------------------------------------------------------------

HISTÓRICO
    20200912: João Paulo, dezembro de 2020.
        - 17.3 – Testando python_repos.py (pg 440).

    20201012: João Paulo, dezembro de 2020.
        - Refatoração do código.
        - Implementação do método setUp()."""


import unittest

from python_repos import chamada_api


class PythonReposTestCase(unittest.TestCase):
    """Testes para 'python_repos.py'."""
    

    def setUp(self):
        """Faz a chamada da API para todos os testes."""
        self.r = chamada_api()
        self.response_dict = self.r.json()


    def test_status_code(self):
        """O valor de status_code é 200?""" 
        self.assertEqual(self.r.status_code, 200)


    def test_num_repos(self):
        """O número total de repositórios é maior que 600000?."""
        # Testa se x >= y
        self.assertGreaterEqual(int(self.response_dict['total_count']), 600000)


    def test_num_itens(self):
        """o número de itens devolvidos é o que se espera?"""
        num_items = len(self.response_dict['items'])
        
        self.assertGreaterEqual(num_items, 20)
        self.assertEqual(num_items, 30)


unittest.main()
