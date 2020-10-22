#! /usr/bin/env python3

"""
NOME
    favorite_fruits - FAÇA VOCÊ MESMO

SINOPSES
    chmod +x favorite_fruits.py
    ./favorite_fruits.ii

    - Você realmente gosta de maçã!

    - Você realmente gosta de bananas!

    - Você realmente gosta de pera!

DESCRIÇÃO
    5.7 – Fruta favorita: Faça uma lista de suas frutas favoritas e, então,
    escreva uma série de instruções if independentes que verifiquem se
    determinadas frutas estão em sua lista.

    • Crie uma lista com suas três frutas favoritas e chame-a de
    favorite_fruits.

    • Escreva cinco instruções if. Cada instrução deve verificar se uma
    determinada fruta está em sua lista. Se estiver, o bloco if deverá exibir
    uma frase, por exemplo, Você realmente gosta de bananas!

HISTÓRICO
    20202210: João Paulo, outubro de 2020.
        - 5.7 – Fruta favorita - Pag. 124.

"""


favorite_fruits = ['maçã', 'pera', 'banana']

if 'maçã' in favorite_fruits: print("\n- Você realmente gosta de maçã!")
if 'banana' in favorite_fruits: print("\n- Você realmente gosta de bananas!")
if 'pera' in favorite_fruits: print("\n- Você realmente gosta de pera!")
if 'manga' in favorite_fruits: print("\n- Você realmente não  gosta de manga!")
if 'mamão' in favorite_fruits: print("\n- Você realmente não gosta de mamão!")
