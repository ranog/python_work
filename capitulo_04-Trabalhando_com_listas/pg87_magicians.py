#! /usr/bin/env python3

"""
NOME
    pg87_magicians.py

SINOPSES
    chmod +x pg87_magicians.py
    ./pg87_magicians.py

DESCRIÇÃO
    Vamos usar um laço for para exibir cada um dos nomes de uma lista de
    mágicos

----------------------------------------------------------------------

HISTÓRICO
    20201310: João Paulo, outubro de 2020.
        - Percorrendo uma lista inteira com um laço;
        - Observando os laços com mais detalhes;
        - Executando mais tarefas em um laço for;
        - Fazendo algo após um laço for;
        - Evitando erros de indentação;
        - Esquecendo-se de indentar;
        - Esquecendo-se de indentar linhas adicionais;
        - Indentando desnecessariamente;
        - Indentando desnecessariamente após o laço;
        - Esquecendo os dois-pontos.

"""


magicians = ['alice', 'david', 'carolina']

print("- Percorrendo uma lista inteira com um laço:")
for magician in magicians:
    print(magician)

print("\n- Executando mais tarefas em um laço for:")
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("- Fazendo algo após um laço for:")
print("Thank you, everyone. That was a great magic show!")
