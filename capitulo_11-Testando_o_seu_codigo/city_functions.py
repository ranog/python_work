#! /usr/bin/env python3

"""
NOME
    city_functions.py - FAÇA VOCÊ MESMO.

------------------------------------------------------------------------

SINOPSES
    from city_functions import city_country

------------------------------------------------------------------------

DESCRIÇÃO
    11.1 – Cidade, país:
        Escreva uma função que aceite dois parâmetros: o nome de uma
        cidade e o nome de um país. A função deve devolver uma única
        string no formado Cidade, País, por exemplo, Santiago, Chile.
        Armazene a função em um módulo chamado city_functions.py.

        Crie um arquivo de nome test_cities.py que teste a função que
        você acabou de escrever (lembre-se de que é necessário importar
        unittest e a função que você quer testar). Escreva um método
        chamado test_city_country() para conferir se a chamada à sua
        função com valores como 'santiago' e 'chile' resulta na string
        correta. Execute test_cities.py e garanta que
        test_city_country() passe no teste.

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
        - 11.1 - Cidade, pais (pg 263).
        - 11.2 – População (pg 263).

------------------------------------------------------------------------

"""


def city_country(city, country, population=''):
    """Devolve uma cidade e um país."""

    if population:
        cities = city.title() + ", " + country.title() + " - população " +\
            str(population) + "."
    else:
        cities = city.title() + ", " + country.title() + "."

    return cities
