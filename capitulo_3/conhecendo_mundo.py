#! /usr/bin/env python3

"""
NOME
    conhecendo_mundo.py

SINOPSES
    chmod +x conhecendo_mundo.py
        ./conhecendo_mundo.py

DESCRIÇÃO
    Capítulo 3 Introdução às listas
        - FAÇA VOCÊ MESMO
            3.8 - Conhecendo o mundo: Pense em pelos menos cinco
            lugares do mundo que você gostaria de visitar.
                ° Armazene as localidades em uma lista. Certifique-se
                de que a lista não esteja em ordem alfabética.
                ° Exiba sua lista na ordem original. Não se preocupe
                em exibir a lista de forma elegante; basta exibi-la
                como uma lista Python pura.
                ° Utilize sorted() para exibir sua lista em ordem
                alfabética, sem modificar a lista propriamente dita
                ° Mostre que sua lista manteve sua ordem original
                exibindo-a.
                ° Utilize sorted() para exibir sua lista em ordem
                alfabética inversa sem alterar a ordem da lista
                original.
                ° Mostre que sua lista manteve sua ordem original
                exibindo-a novamente.
                ° Utilize reverse() para mudar a ordem de sua lista.
                Exiba a lista para mostrar que sua ordem mudou.
                ° Utilize reverse() para mudar a ordem de sua lista
                novamente. Exiba a lista para mostrar que ela voltou à
                sua ordem original.
                ° Utilize sort() para mudar sua lista de modo que ela
                seja armazenada em ordem alfabética inversa. Exiba a
                lista para mostrar que sua ordem mudou.

            3.9 - Convidados para o jantar: Trabalhando, com um dos
            programas dos Exercícios de 3.4 a 3.7 (página 80 e 81),
            use len() para exibir uma mensagem informando o número de
            pessoas que você está convidando para o jantar.

            3.10 - Todas as funções: Pensa em algo que você poderia
            armazenar em uma lista. Por exemplo, você poderia criar
            umas lista de montanhas, rios, países, cidades, idiomas
            ou qualquer outro item que quiser. Escreva um programa que
            quiser. Escreva um programa que crie uma lista contendo
            esses itens e então utilize cada função apresentada
            neste capítulo pelo menos uma vez.

-----------------------------------------------------------------------

HISTÓRICO
    20200402: João Paulo, fevereiro de 2020
        - Implementação dos exercicios "FAÇA VOCÊ MESMO"
            ° 3.8 - Conhecendo o mundo
            ° 3.9 - Convidados para o jantar
            ° 3.10 - Todas as funções

    20200902: João Paulo, fevereiro de 2020.
        - Implementação do exercício 3.8, pag. 83 
"""


capitais = ["tallinn, estônia", "nova York, estados unidos",
            "innsbruck, áustria", "berlim, alemanha",
            "toronto, canadá"]

print("\nOrdem original:\n" + str(capitais))

print("\nOrdem alfabética:\n" + str(sorted(capitais)))

print("\nOrdem original:\n" + str(capitais))

print("\nOrdem alfabética inversa com o sorted():\n" +
        str(sorted(capitais, reverse=True)))

print("\nOrdem original:\n" + str(capitais))

print("\nMudar a ordem da lista: ")
capitais.reverse()
print(capitais)

capitais.reverse()
print("\nMudar a ordem da lista novamente:\n" + str(capitais))
