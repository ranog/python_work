#! /usr/bin/env python3

"""
NOME
    ferias.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x ferias.py
    ./ferias.py

    7.10 - Férias dos sonhos:

    Qual é o seu nome?  joão paulo
    Se pudesse visitar um lugar do mundo, para onde você iria? bélgica
    Você gostaria de deixar outra pessoa responder (sim|não)? não

    --- Resultado da enquete ---

    João Paulo iria para: Bélgica.

DESCRIÇÃO
    FAÇA VOCÊ MESMO

    7.10 – Férias dos sonhos: Escreva um programa que faça uma enquete
    sobre as férias dos sonhos dos usuários. Escreva um prompt
    semelhante a este: Se pudesse visitar um lugar do mundo, para onde
    você iria? Inclua um bloco de código que apresente os resultados da
    enquete.

HISTÓRICO
    20200111: João Paulo, outubro de 2020.
        - 7.10 - Férias dos sonhos (pg 167).

"""


print("\n7.10 - Férias dos sonhos: ")

respostas = {}
chave = True

while chave:
    nome = input("\nQual é o seu nome?  ")
    lugar = input("Se pudesse visitar um lugar do mundo, para onde você iria? ")

    respostas[nome] = lugar

    repetir = input("Você gostaria de deixar outra pessoa responder (sim|não)? ")
    if repetir.lower() == 'não' or repetir.lower() == 'nao':
        chave = False

print("\n--- Resultado da enquete ---\n")
for nome, lugar in respostas.items():
    print(nome.title() + " iria para: " + lugar.title() + ".")
