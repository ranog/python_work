#! /usr/bin/env python3

"""
NOME
    user_profile.py - Usando argumentos nomeados arbitrários.

SINOPSES
    chmod +x user_profile.py
    ./user_profile.py
    {'first_name': 'albert', 'last_name': 'einstein',
    'location': 'princeton', 'field': 'physics'}

DESCRIÇÃO
    A definição de build_profile() espera um primeiro nome e um
    sobrenome e permite que o usuário passe tantos pares nome-valor
    quantos ele quiser. Os asteriscos duplos antes do parâmetro
    **user_info fazem Python criar um dicionário vazio chamado user_info
    e colocar quaisquer pares nome-valor recebidos nesse dicionário.
    Nessa função, podemos acessar os pares nome-valor em user_info como
    faríamos com qualquer dicionário.

HISTÓRICO
    20200711: João Paulo, outubro de 2020.
        - Usando argumentos nomeados arbitrários (pg 189-190).

"""


def build_profile(first, last, **user_info):
    """Constrói um dicionário contendo tudo que sabemos sobre um
    usuário."""

    profile = {}

    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value

    return profile

user_profile = build_profile('albert', 'einstein',
                             location = 'princeton', field = 'physics')

print(user_profile)
