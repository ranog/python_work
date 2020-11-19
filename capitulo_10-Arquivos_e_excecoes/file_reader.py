#! /usr/bin/env python3

"""
NOME
    file_reader.py - Lendo um arquivo inteiro.

SINOPSES
    chmod +x file_reader.py
    ./file_reader.py
    3.1415926535
    8979323846
    2643383279

    3.1415926535
    8979323846
    2643383279

------------------------------------------------------------------------

DESCRIÇÃO
    Para realizar qualquer tarefa com um arquivo, mesmo que seja apenas
    exibir o seu conteúdo, você precisará inicialmente abrir o arquivo
    para acessá-lo. 

    A função open() precisa de um argumento: o nome do arquivo que você
    quer abrir. Python procura esse arquivo no diretório em que o
    programa executando no momento está armazenado. Nesse exemplo,
    file_reader.py está executando, portanto Python procura
    pi_digits.txt no diretório em que o arquivo file_reader.py está
    armazenado. A função open() devolve um objeto que representa o
    arquivo. Nesse caso, open('pi_digits.txt') devolve um objeto que
    representa pi_digits.txt. Python armazena esse objeto em
    file_object.

    A palavra reservada with fecha o arquivo depois que não for mais
    necessário acessá-lo. Observe como chamamos open() nesse programa,
    mas não chamamos close(). Você poderia abrir e fechar o arquivo
    chamando open() e close(), mas se um bug em seu programa impedir que
    a instrução close() seja executada, o arquivo não será fechado. Isso
    pode parecer trivial, mas arquivos indevidamente fechados podem
    provocar perda de dados ou estes podem ser corrompidos. Além disso,
    se close() for chamado cedo demais em seu programa, você se verá
    tentando trabalhar com um arquivo fechado (um arquivo que não pode
    ser acessado), o que resultará em mais erros. Nem sempre é fácil
    saber exatamente quando devemos fechar um arquivo, mas com a
    estrutura mostrada aqui, Python descobrirá isso para você. Tudo que
    você precisa fazer é abrir o arquivo e trabalhar com ele conforme
    desejado, com a confiança de que Python o fechará automaticamente no
    momento certo.

    Depois que tivermos um objeto arquivo que represente pi_digits.txt,
    usamos o método read() na segunda linha de nosso programa para ler
    todo o conteúdo do arquivo e armazená-lo em uma longa string em
    contents. Quando exibimos o valor de contents, vemos o arquivo-texto
    completo.

    A única diferença entre essa saída e o arquivo original é a linha em
    branco extra no final da saída. A linha em branco aparece porque
    read() devolve uma string vazia quando alcança o final do arquivo;
    essa string vazia aparece como uma linha em branco. Se quiser
    remover essa linha em branco extra, rstrip() pode ser usada na
    instrução print.

------------------------------------------------------------------------

HISTÓRICO
    20201911: João Paulo, novembro de 2020.
        - Lendo um arquivo inteiro (pg 230-231).

"""


with open('pi_digits.txt') as file_object:
    contents = file_object.read()

    print(contents)
   
    # XXX O método rstrip() de Python remove qualquer caractere branco
    # do lado direito de uma string. Agora a saída será exatamente igual
    # ao conteúdo do arquivo original:
    print(contents.rstrip())
