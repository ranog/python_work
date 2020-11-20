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
    3.141592653589793238462643383279
    32

------------------------------------------------------------------------

DESCRIÇÃO
    - Lendo um arquivo inteiro: 
        Para realizar qualquer tarefa com um arquivo, mesmo que seja
        apenas exibir o seu conteúdo, você precisará inicialmente abrir
        o arquivo para acessá-lo. 

        A função open() precisa de um argumento: o nome do arquivo que
        você quer abrir. Python procura esse arquivo no diretório em que
        o programa executando no momento está armazenado. Nesse exemplo,
        file_reader.py está executando, portanto Python procura
        pi_digits.txt no diretório em que o arquivo file_reader.py está
        armazenado. A função open() devolve um objeto que representa o
        arquivo. Nesse caso, open('pi_digits.txt') devolve um objeto que
        representa pi_digits.txt. Python armazena esse objeto em
        file_object.

        A palavra reservada with fecha o arquivo depois que não for mais
        necessário acessá-lo. Observe como chamamos open() nesse
        programa, mas não chamamos close(). Você poderia abrir e fechar
        o arquivo chamando open() e close(), mas se um bug em seu
        programa impedir que a instrução close() seja executada, o
        arquivo não será fechado. Isso  pode parecer trivial, mas
        arquivos indevidamente fechados podem provocar perda de dados ou
        estes podem ser corrompidos. Além disso, se close() for chamado
        cedo demais em seu programa, você se verá tentando trabalhar com
        um arquivo fechado (um arquivo que não pode ser acessado), o que
        resultará em mais erros. Nem sempre é fácil saber exatamente
        quando devemos fechar um arquivo, mas com a estrutura mostrada
        aqui, Python descobrirá isso para você. Tudo que você precisa
        fazer é abrir o arquivo e trabalhar com ele conforme desejado,
        com a confiança de que Python o fechará automaticamente no
        momento certo.

        Depois que tivermos um objeto arquivo que represente
        pi_digits.txt, usamos o método read() na segunda linha de nosso
        programa para ler todo o conteúdo do arquivo e armazená-lo em
        uma longa string em contents. Quando exibimos o valor de
        contents, vemos o arquivo-texto completo.

        A única diferença entre essa saída e o arquivo original é a
        linha em branco extra no final da saída. A linha em branco
        aparece porque read() devolve uma string vazia quando alcança o
        final do arquivo; essa string vazia aparece como uma linha em
        branco. Se quiser remover essa linha em branco extra, rstrip()
        pode ser usada na instrução print.


    - Lendo dados linha a linha:
        Armazenamos o nome do arquivo que estamos lendo em uma variável
        filename. Essa é uma convenção comum quando trabalhamos com
        arquivos. Como a variável filename não representa o arquivo
        propriamente dito – é apenas uma string que diz a Python em que
        lugar o arquivo se encontra – você pode facilmente trocar
        'pi_digits.txt' pelo nome de outro arquivo com o qual você
        queira trabalhar. Depois da chamada a open(), um objeto que
        representa o arquivo e seu conteúdo é armazenado na variável
        file_object. Novamente, usamos a sintaxe with para deixar Python
        abrir e fechar o arquivo de modo apropriado. Para analisar o
        conteúdo do arquivo, trabalhamos com cada linha do arquivo
        percorrendo o objeto arquivo em um laço.


    - Criando uma lista de linhas de um arquivo:
        O método readlines() armazena cada linha do arquivo em uma
        lista. Essa lista é então armazenada em lines, com a qual
        podemos continuar trabalhando depois que o bloco with terminar.
        Usamos um laço for simples para exibir cada linha de lines.
        Como cada item de lines corresponde a uma linha do arquivo, a
        saída será exatamente igual ao conteúdo do arquivo.


    - Trabalhando como conteúdo de um arquivo:

        Começamos abrindo o arquivo e armazenando cada linha de dígitos
        em uma lista, como fizemos no exemplo anterior. Em u criamos uma
        variável pi_string para armazenar os dígitos de pi. Então
        criamos um laço que acrescenta cada uma das linhas de dígitos em
        pi_string removendo o caractere de quebra de linha. Exibimos
        essa string e mostramos também o seu tamanho.
        
    NOTA:
        Quando Python lê um arquivo-texto, todo o texto do arquivo é
        interpretado como uma string. Se você ler um número e quiser
        trabalhar com esse valor em um contexto numérico, será
        necessário convertê-lo em um inteiro usando a função int() ou
        convertê-lo em um número de
ponto flutuante com a função float(). 

------------------------------------------------------------------------

HISTÓRICO
    20201911: João Paulo, novembro de 2020.
        - Lendo um arquivo inteiro (pg 230-231).
        - Lendo dados linha a linha (pg 233-234).

    20202011: João Paulo, novembro de 2020.
        - Criando uma lista de linhas de um arquivo (pg 234-235).
        - Trabalhando como conteúdo de um arquivo (pg 235).

"""

"""
with open('pi_digits.txt') as file_object:
    contents = file_object.read()

    print(contents)
   
    # XXX O método rstrip() de Python remove qualquer caractere branco
    # do lado direito de uma string. Agora a saída será exatamente igual
    # ao conteúdo do arquivo original:
    print(contents.rstrip())
"""

filename = 'pi_digits.txt'

"""
with open(filename) as file_object:

    for line in file_object:
        print(line.rstrip()) # XXX Se usarmos rstrip() em cada linha na
        # instrução print, eliminamos essas linhas em branco extras.
"""

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())


pi_string = ''

for line in lines:
    pi_string += line.strip() # tira os espaços em branco

print(pi_string)
print(len(pi_string))
