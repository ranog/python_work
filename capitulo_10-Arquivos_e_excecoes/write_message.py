#! /usr/bin/env python3

"""
NOME
    write_message.py - Escrevendo dados em um arquivo vazio.

SINOPSES
    chmod +x write_message.py
    ./write_message.py

------------------------------------------------------------------------

DESCRIÇÃO
    - Escrevendo dados em um arquivo vazio:
        A chamada a open() nesse exemplo tem dois argumentos. O primeiro
        argumento ainda é o nome do arquivo que queremos abrir. O
        segundo argumento, 'w', diz a Python que queremos abrir o
        arquivo em modo de escrita. Podemos abrir um arquivo em modo de
        leitura ('r'), em modo de escrita ('w'), em modo de concatenação
        ('a') ou em um modo que permita ler e escrever no arquivo
        ('r+'). Se o argumento de modo for omitido, por padrão Python
        abrirá o arquivo em modo somente de leitura.

        A função open() cria automaticamente o arquivo no qual você vai
        escrever caso ele ainda não exista. No entanto, tome cuidado ao
        abrir um arquivo em modo de escrita ('w') porque se o arquivo já
        existir, Python o apagará antes de devolver o objeto arquivo.
        Usamos o método write() no objeto arquivo para escrever uma
        string nesse arquivo. Esse programa não tem saída no terminal,
        mas se abrir o arquivo programming.txt, você verá uma linha:
        programming.txt I love programming.

        Esse arquivo se comporta como qualquer outro arquivo de seu
        computador. Você pode abri-lo, escrever um novo texto nele,
        copiar ou colar dados e assim por diante.


    - NOTA:
        Python escreve apenas strings em um arquivo-texto. Se quiser
        armazenar dados numéricos em um arquivo-texto, será necessário
        converter os dados em um formato de string antes usando a função
        str().

------------------------------------------------------------------------

HISTÓRICO
    20202111: João Paulo, novembro de 2020.
        - Escrevendo dados em um arquivo vazio (pg 237-238).
        - Escrevendo várias linhas (pg 238-239).

"""


filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
