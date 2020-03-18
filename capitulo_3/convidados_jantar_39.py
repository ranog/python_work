#! /usr/bin/env python3

"""
NOME
    convidados_jantar_39.py

SINOPSES
    chmod +x convidados_jantar_39.py
        ./convidados_jantar_39.py
        3.4 - Lista de convidados:
            João vamos jantar hoje?
            Paulo vamos jantar hoje?
            João Paulo vamos jantar hoje?

        3.5 - Alterando a lista de convidados:
            João não poderá comparecer.

            Paulo João vai ao jantar.
            Paulo vai ao jantar.
            João Paulo vai ao jantar.

        3.6 - Mais convidados:
            Encontrei uma mesa de jantar maior.

            Johnny vai ao jantar.
            Paulo João vai ao jantar.
            Paul vai ao jantar.
            Paulo vai ao jantar.
            João Paulo vai ao jantar.
            Jp vai ao jantar.

        3.7 - Reduzindo a lista de convidados:
            Pesso desculpa a todos, mas só posso convidar apenas duas pessoas para o jantar.

            Johnny sinto muito por não poder convidá-lo para o jantar.
            Paulo João sinto muito por não poder convidá-lo para o jantar.
            Paul sinto muito por não poder convidá-lo para o jantar.
            Paulo sinto muito por não poder convidá-lo para o jantar.

            João Paulo ainda vamos jantar.
            Jp ainda vamos jantar.

            Lista de convidados: []

    DESCRIÇÃO
        O programa demonstra a inserção e remoção de itens em uma lista.

----------------------------------------------------------------------

    HISTÓRICO
        20202801: João Paulo, janeiro de 2020
            - Capítulo 3 / Introdução às listas
                - FAÇA VOCÊ MESMO
                    - Pag. 79: 3.4
                    - Pag. 79: 3.5
                    - Pag. 79: 3.6
                    - Pag. 80: 3.7

        20203001: João Paulo, janeiro de 2020
            - Resolução dos exercícios da Pag. 79-80
                - 3.4 - Lista de convidados;
                - 3.5 - Alterando a lista de convidados;
                - 3.6 - Mais convidados;
                - 3.7 - Reduzindo a lista de convidados.

        20201703: João Paulo, março de 2020.
            - Implementação da função len() para exibir o número de pessoas
              convidadas.
"""

convidados = ["joão", "paulo" , "joão paulo"]

print("\n 3.4 - Lista de convidados:")

print("\t" + convidados[0].title() + " vamos jantar hoje?")
print("\t" + convidados[1].title() + " vamos jantar hoje?")
print("\t" + convidados[2].title() + " vamos jantar hoje?")
print("\n\t- " + str(len(convidados)) + " pessoas foram convidadas.\n")

print("\n 3.5 - Alterando a lista de convidados:")

print("\t" + convidados[0].title() + " não poderá comparecer.\n")

convidados[0] = "paulo joão"

print("\t" + convidados[0].title() + " vai ao jantar.")
print("\t" + convidados[1].title() + " vai ao jantar.")
print("\t" + convidados[2].title() + " vai ao jantar.")
print("\n\t- " + str(len(convidados)) + " pessoas foram convidadas.\n")

print("\n 3.6 - Mais convidados:")

print("\tEncontrei uma mesa de jantar maior.\n")

convidados.insert(0, "johnny")
convidados.insert(2, "paul")
convidados.append("jp")

print("\t" + convidados[0].title() + " vai ao jantar.")
print("\t" + convidados[1].title() + " vai ao jantar.")
print("\t" + convidados[2].title() + " vai ao jantar.")
print("\t" + convidados[3].title() + " vai ao jantar.")
print("\t" + convidados[4].title() + " vai ao jantar.")
print("\t" + convidados[5].title() + " vai ao jantar.")
print("\n\t- " + str(len(convidados)) + " pessoas foram convidadas.\n")


print("\n 3.7 - Reduzindo a lista de convidados:")

print("\tPesso desculpa a todos, mas só posso convidar apenas duas pessoas para o jantar.\n")


print("\t" + convidados.pop(0).title() + " sinto muito por não poder convidá-lo para o jantar.")
print("\t" + convidados.pop(0).title() + " sinto muito por não poder convidá-lo para o jantar.")
print("\t" + convidados.pop(0).title() + " sinto muito por não poder convidá-lo para o jantar.")
print("\t" + convidados.pop(0).title() + " sinto muito por não poder convidá-lo para o jantar.\n")

print("\t" + convidados[0].title() + " ainda vamos jantar.")
print("\t" + convidados[1].title() + " ainda vamos jantar.")

del convidados[0]
del convidados[0]


print("\n\tLista de convidados: " + str(convidados))
print("\n\t- " + str(len(convidados)) + " pessoas foram convidadas.\n")
