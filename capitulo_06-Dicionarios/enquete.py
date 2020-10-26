#! /usr/bin/env python3

"""
NOME
    enquete.py - FAÇA VOCÊ MESMO

SINOPSES
    chmod +x enquete.py
    ./enquete.py

DESCRIÇÃO

HISTÓRICO
    20202610: João Paulo, outubro de 2020
        - FAÇA VOCÊ MESMO 6.6 - Enquete (pg 143).

"""


rios = {'amazonas' : 'brasil', 
        'mississipi' : 'estados unidos',
        'danúbio' : 'alemanha',}

for rio, pais in rios.items():
    if pais.lower() == 'alemanha':
        print("O " + rio.title() + " corre pela " + pais.title() + ".")
    else:
        print("O " + rio.title() + " corre pelo " + pais.title() + ".")
