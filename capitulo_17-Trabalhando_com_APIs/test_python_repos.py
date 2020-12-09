#! /usr/bin/env python3

"""
NOME
    test_python_repos.py - FAÇA VOCÊ MESMO.

SINOPSES
    $ chmod +x test_python_repos.py
    $ ./test_python_repos.py

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

"""


import unittest
import requests

import python_repos


class PythonReposTestCase(unittest.TestCase):
    """Testes para 'python_repos.py'."""

    def test_status_code(self):
        """O valor de status_code é 200?""" 
        
        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'   
        r = requests.get(url)
        self.assertEqual(r.status_code, 200)

"""
    def test_first_last_middle_name(self):
        Nomes como 'Wolfgang Amadeus Mozart' funcionam?

        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
"""

unittest.main()
