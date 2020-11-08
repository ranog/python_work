#! /usr/bin/env python3

"""
NOME
    perfil_usuario.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x perfil_usuario.py
    ./perfil_usuario.py

DESCRIÇÃO
    8.13 – Perfil do usuário: Comece com uma cópia de user_profile.py,
    da página 210. Crie um perfil seu chamando build_profile(), usando
    seu primeiro nome e o sobrenome, além de três outros pares
    chave-valor que o descrevam.

HISTÓRICO
    20200711: João Paulo, outubro de 2020.
        - 8.13 - Perfil do usuário (pg 190).

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

user_profile = build_profile('john', 'ranog',
                             username = 'johnny', gamer = 'diablo',
                             programmer = 'python')

print(user_profile)
