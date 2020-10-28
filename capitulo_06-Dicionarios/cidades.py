#! /usr/bin/env python3

"""
NOME
    cidades.py - FAÇA VOCÊ MESMO

SINOPSES
    chmod +x cidades.py
    ./cidades.py

    Cidade: Chongging
    - País: China
    - População: 30.165.500
    - Definição: Município Autônomo

    Cidade: Xangai
    - País: China
    - População: 17.836.133
    - Definição: Município Autônomo

    Cidade: Lagos
    - País: Nigéria
    - População: 16.060.307
    - Definição: Divisão Administrativa Nacional

DESCRIÇÃO
    6.11 – Cidades: Crie um dicionário chamado cities. Use os nomes de
    três cidades como chaves em seu dicionário. Crie um dicionário com
    informações sobre cada cidade e inclua o país em que a cidade está
    localizada, a população aproximada e um fato sobre essa cidade. As
    chaves do dicionário de cada cidade devem ser algo como country,
    population e fact. Apresente o nome de cada cidade e todas as
    informações que você armazenou sobre ela.

HISTÓRICO
    20202810: João Paulo, outubro de 2020.
        - FAÇA VOCÊ MESMO / 6.11 - Cidades (pg 150).

"""


cities = {
    'chongging' : {'country' : 'china', 'population' : '30.165.500',
        'fact' : 'município autônomo',},
    'xangai' : {'country' : 'china', 'population' : '17.836.133',
        'fact' : 'município autônomo',},
    'lagos' : {'country' : 'nigéria', 'population' : '16.060.307',
        'fact' : 'divisão administrativa nacional',},}

for name, info in cities.items():
    print("\nCidade: " + name.title())
    print("- País: " + info['country'].title())
    print("- População: " + info['population'])
    print("- Definição: " + info['fact'].title())
