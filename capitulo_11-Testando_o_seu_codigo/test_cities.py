#! /usr/bin/env python3

"""
NOME
    test_cities_.py - FAÇA VOCÊ MESMO.

------------------------------------------------------------------------

SINOPSES
    $ chmod +x test_cities.py
    $ ./test_cities.py
    .
    --------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK

------------------------------------------------------------------------

    E
    ====================================================================
    ERROR: test_city_country (__main__.CityCountryTestCase)
    Strings no formato Cidade, País funcionam?
    --------------------------------------------------------------------
    Traceback (most recent call last):
        File "./test_cities.py", line 52, in test_city_country
            cities_countries = city_country('santiago', 'chile')
    TypeError: city_country() missing 1 required positional argument:
    'population'

    --------------------------------------------------------------------
    Ran 1 test in 0.001s

    FAILED (errors=1)

    --------------------------------------------------------------------

------------------------------------------------------------------------

    .
    --------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK

------------------------------------------------------------------------

    ..
    --------------------------------------------------------------------
    Ran 2 tests in 0.000s

    OK

------------------------------------------------------------------------

DESCRIÇÃO
    11.1 – Cidade, país:
        Escreva uma função que aceite dois parâmetros: o nome de uma
        cidade e o nome de um país. A função deve devolver uma única
        string no formado Cidade, País, por exemplo, Santiago, Chile.
        Armazene a função em um módulo chamado city_functions.py. Crie
        um arquivo de nome test_cities.py que teste a função que você
        acabou de escrever (lembre-se de que é necessário importar
        unittest e a função que você quer testar). Escreva um método
        chamado test_city_country() para conferir se a chamada à sua
        função com valores como 'santiago' e 'chile' resulta na string
        correta. Execute test_cities.py e garanta que
        test_city_country() passe no teste.

------------------------------------------------------------------------

    11.2 – População:
        Modifique sua função para que ela exija um terceiro parâmetro,
        population. Agora ela deve devolver uma única string no formato
        Cidade, País – população xxx, por exemplo, Santiago, Chile –
        população 5000000. Execute test_cities.py novamente.
        Certifique-se de que test_city_country() falhe dessa vez.

        Modifique a função para que o parâmetro population seja
        opcional. Execute test_cities.py novamente e garanta que
        test_city_country() passe novamente. Escreva um segundo teste
        chamado test_city_country_population() que verifique se você
        pode chamar sua função com os valores 'santiago', 'chile' e
        'population=5000000'. Execute test_cities.py novamente e garanta
        que esse novo teste passe.

------------------------------------------------------------------------

HISTÓRICO
    20202711: João Paulo, novembro de 2020.
        - 11.1 – Cidade, país (pg 263).
        - 11.2 – População (pg 262-264).

------------------------------------------------------------------------

"""


import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Testes para 'city_functions.py'.'"""

    def test_city_country(self):
        """Strings no formato Cidade, País funcionam?"""

        cities = city_country('santiago', 'chile')
        self.assertEqual(cities, 'Santiago, Chile.')


    def test_city_country_population(self):
        """Strings no formato Cidade, País - população xxx funcionam?"""

        cities = city_country('santiago', 'chile', 5000000)
        self.assertEqual(cities, 'Santiago, Chile - população 5000000.')


unittest.main()
