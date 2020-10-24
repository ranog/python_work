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

----------------------------------------------------------------------

HISTÓRICO
    20202410: João Paulo, outubro de 2020.
        - Percorrendo todos os pares chave-valor com um laço
        (Pag. 138-139).

"""


user_0 = {'username' : 'efermi', 'first' : 'enrico', 'last' : 'fermi',}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
