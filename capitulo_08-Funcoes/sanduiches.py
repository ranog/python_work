#! /usr/bin/env python3

"""
NOME
    sanduiches.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x sanduiches.py
    ./sanduiches.py

    BLT (Estados Unidos):
    - Pão de forma tostado
    - Maionese
    - Bacon
    - Alface (lettuce)
    - Tomate

    Cemita (México):
    - Pão tipo brioche (ou cemita)
    - Abacate
    - Carne (geralmente carne bovina e frita)
    - Queijo branco
    - Cebola
    - Ervas
    - Molho de tomate
    - Pimentão

    Croque Madame (França):
    - Pão de forma
    - Presunto grelhado
    - Queijos (emmental e gruyère)
    - Molho bechamel
    - Ovo frito

    Bauru (Brasil):
    - Pão francês
    - Rosbife
    - Tomate fatiado
    - Picles
    - Mistura de queijos (prato, estepe, gouda e suíço) derretidos em
    banho-maria

    Fischbrötchen (Alemanha):
    - Pão crocante
    - Peixe (arenque em conserva, espadilha europeia, salmão fumado,
    cavala) ou até mesmo camarão
    - Cebola
    - Molho rémoulade (que tem como base a maionese)
    - Picles


DESCRIÇÃO
    8.12 – Sanduíches: Escreva uma função que aceite uma lista de itens
    que uma pessoa quer em um sanduíche. A função deve ter um parâmetro
    que agrupe tantos itens quantos forem fornecidos pela chamada da
    função e deve apresentar um resumo do sanduíche pedido. Chame a
    função três vezes usando um número diferente de argumentos a cada
    vez.

HISTÓRICO
    20200711: João Paulo, outubro de 2020.
        - 8.12 - Sanduíches (pg 190).

"""


def sanduiche(*ingredientes):
    for ingrediente in ingredientes:
        print("- " + ingrediente)


print("\nBLT (Estados Unidos): ")
sanduiche('Pão de forma tostado', 'Maionese', 'Bacon', 'Alface (lettuce)',
           'Tomate')

print("\nCemita (México): ")
sanduiche('Pão tipo brioche (ou cemita)', 'Abacate',
           'Carne (geralmente carne bovina e frita)', 'Queijo branco',
           'Cebola', 'Ervas', 'Molho de tomate', 'Pimentão')

print("\nCroque Madame (França): ")
sanduiche('Pão de forma', 'Presunto grelhado', 'Queijos (emmental e gruyère)',
          'Molho bechamel', 'Ovo frito')

print("\nBauru (Brasil): ")
sanduiche('Pão francês', 'Rosbife', 'Tomate fatiado', 'Picles',
          'Mistura de queijos (prato, estepe, gouda e suíço) derretidos em banho-maria')

print("\nFischbrötchen (Alemanha): ")
sanduiche('Pão crocante',
          'Peixe (arenque em conserva, espadilha europeia, salmão fumado, cavala) ou até mesmo camarão',
          'Cebola', 'Molho rémoulade (que tem como base a maionese)', 'Picles')
