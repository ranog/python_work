#! /usr/bin/env python3

"""
NOME
    user.py - Percorrendo todos os pares chave-valor com um laço

SINOPSES
    chmod +x user.py
    ./user.py

    Key: username
    Value: efermi

    Key: first
    Value: enrico

    Key: last
    Value: fermi

    - 6.12 - Extensões:

    Username: efermi
    Name: Erico Fermi

    Username: aeinstein
    Name: Albert Einstein

    Username: mcurie
    Name: Marie Curie

DESCRIÇÃO
    Para escrever um laço for para um dicionário, devemos criar nomes
    para as duas variáveis que armazenarão a chave e o valor de cada par
    chave-valor. Você pode escolher qualquer nome que quiser para essas
    duas variáveis. Esse código também funcionaria bem se usássemos
    abreviaturas para os nomes das variáveis, assim: for k, v in
    user_0.items(). A segunda metade da instrução for inclui o nome do
    dicionário, seguido do método items(), que devolve uma lista de
    pares chave-valor. O laço for então armazena cada um desses pares
    nas duas variáveis especificadas. No exemplo anterior, usamos as
    variáveis para exibir cada chave (key), seguido do valor associado
    (value). O "\n" na primeira instrução print garante que uma linha em
    branco seja inserida antes de cada par chave-valor na saída.

    Python não se importa com a ordem em que os pares chave-valor são
    armazenados; ele só registra as conexões entre cada chave individual
    e seu valor.

    6.12 – Extensões: Estamos trabalhando agora com exemplos complexos o
    bastante para poderem ser estendidos de várias maneiras. Use um dos 
    programas de exemplo deste capítulo e estenda-o acrescentando novas
    chaves e valores, alterando o contexto do programa ou melhorando a
    formatação da saída.

----------------------------------------------------------------------

HISTÓRICO
    20202410: João Paulo, outubro de 2020.
        - Percorrendo todos os pares chave-valor com um laço
        (Pag. 138-139).

    20202810: João Paulo, outubro de 2020.
        - FAÇA VOCÊ MESMO 6.12 - Extensões (pg 150).

"""


user_0 = {'username' : 'efermi', 'first' : 'enrico', 'last' : 'fermi',}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

print("\n- 6.12 - Extensões:")

users = {
        'efermi' : {'first' : 'erico', 'last' : 'fermi',},

        'aeinstein' : {'first' : 'albert', 'last': 'einstein',},

        'mcurie': {'first': 'marie', 'last': 'curie',},}

for key, value in users.items():
    print("\nUsername: " + key)

    full_name = value['first'] + " " + value['last']
    print("Name: " + full_name.title())
