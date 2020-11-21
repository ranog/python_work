#! /usr/bin/env python3

"""
NOME
    aprendendo_python.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x aprendendo_python.py
    ./aprendendo_python.py
    - Exibe o conteúdo uma vez lendo o arquivo todo:
    Em Python podemos representar um string colando-o entre aspas ou
    apóstrofes.
    Em Python podemos colocar um else no laço de repetição e que será
    executado no final da iteração.
    Em Python podemos usar variáveis também para armazenar e processar
    textos.
    Em Python podemos ter listas de números, strings e também de valores
    booleanos. 
    Em Python podemos usar and para exigir que duas condições sejam
    verdadeiras ao mesmo tempo.
    Em Python podemos usar o método findall() para extrair todas as
    substrings que correspondem à expressão regular.
    Em Python podemos usar uma estrutura while ou uma estrutura for.
    Em Python podemos implementar e definir a funcionalidade de diversos
    operadores como +, *,. == como parte de nossas classes.

    - Percorrendo o objeto arquivo com um laço:
    Em Python podemos representar um string colando-o entre aspas ou
    apóstrofes.
    Em Python podemos colocar um else no laço de repetição e que será
    executado no final da iteração.
    Em Python podemos usar variáveis também para armazenar e processar
    textos.
    Em Python podemos ter listas de números, strings e também de valores
    booleanos.
    Em Python podemos usar and para exigir que duas condições sejam
    verdadeiras ao mesmo tempo.
    Em Python podemos usar o método findall() para extrair todas as
    substrings que correspondem à expressão regular.
    Em Python podemos usar uma estrutura while ou uma estrutura for.
    Em Python podemos implementar e definir a funcionalidade de diversos
    operadores como +, *,. == como parte de nossas classes.

    - Armazena as linhas em uma lista e então trabalha com elas fora do
    bloco with:
    Em Python podemos representar um string colando-o entre aspas ou
    apóstrofes.Em Python podemos colocar um else no laço de repetição e
    que será executado no final da iteração.Em Python podemos usar
    variáveis também para armazenar e processar textos.Em Python podemos
    ter listas de números, strings e também de valores booleanos.Em
    Python podemos usar and para exigir que duas condições sejam
    verdadeiras ao mesmo tempo.Em Python podemos usar o método findall()
    para extrair todas as substrings que correspondem à expressão
    regular.Em Python podemos usar uma estrutura while ou uma estrutura
    for.Em Python podemos implementar e definir a funcionalidade de
    diversos operadores como +, *,. == como parte de nossas classes.

------------------------------------------------------------------------

DESCRIÇÃO
    10.1 – Aprendendo Python: Abra um arquivo em branco em seu editor de
    texto e escreva algumas linhas que sintetizem o que você aprendeu
    sobre Python até agora. Comece cada linha com a expressão Em Python
    podemos.... Salve o arquivo como learning_python.txt no mesmo
    diretório em que estão seus exercícios deste capítulo. Escreva um
    programa que leia o arquivo e mostre o que você escreveu, três
    vezes. Exiba o conteúdo uma vez lendo o arquivo todo, uma vez percorrendo o
    objeto arquivo com um laço e outra armazenando as linhas em uma
    lista e então trabalhando com ela fora do bloco with.

------------------------------------------------------------------------

HISTÓRICO
    20202011: João Paulo, novembro de 2020.
        - 10.1 – Aprendendo Python (pg 237).

"""


filename = 'learning_python.txt'

with open(filename) as file_object_1:
    print("\n- Exibe o conteúdo uma vez lendo o arquivo todo: ")
    contents = file_object_1.read()
    print(contents.strip())

with open(filename) as file_object_2:
    print("\n- Percorrendo o objeto arquivo com um laço: ")
    for line in file_object_2:
        print(line.rstrip())

with open(filename) as file_object_3:
    lines = file_object_3.readlines()

print("\n- Armazena as linhas em uma lista e então trabalha com elas fora do bloco with: ")

learning = ''

for line in lines:
    learning += line.strip()

print(learning)
