#! /usr/bin/env python3

"""
NOME
    favorite_languages.py - Um dicionário de objetos semelhantes

SINOPSES
    chmod +x favorite_languages.py
    ./favorite_languages.py

    - Sarah's favorite language is C.

    Jen's favorite language is Python.
    Sarah's favorite language is C.
    Edward's favorite language is Ruby.
    Phil's favorite language is Python.

    Jen
    Sarah
    Edward
    Phil

    Jen
    Sarah
     Hi Sarah, I see your favorite language is C!
    Edward
    Phil
     Hi Phil, I see your favorite language is Python!

    Erin, please take our poll!

    Edward, thank you for taking the poll.
    Jen, thank you for taking the poll.
    Phil, thank you for taking the poll.
    Sarah, thank you for taking the poll.

    The following languages have been mentioned:
    Python
    C
    Ruby
    Python

    The following languages have been mentioned:
    C
    Ruby
    Python

    - Jen obrigado por responder nossa enquete.

    - Sarah obrigado por responder nossa enquete.

    - Edward sua participação é muito importante.

    - Phil sua participação é muito importante.

DESCRIÇÃO
    - Um dicionário de objetos semelhantes

    Quando souber que precisará de mais de uma linha para definir um
    dicionário, tecle ENTER depois da chave de abertura. Em seguida,
    indente a próxima linha em um nível (quatro espaços) e escreva o
    primeiro par chave-valor, seguido de uma vírgula. A partir desse
    ponto, quando pressionar ENTER , seu editor de texto deverá indentar
    automaticamente todos os pares chave-valor subsequentes para que
    estejam de acordo com o primeiro par chave-valor.

    Depois que acabar de definir o dicionário, acrescente uma chave de
    fechamento em uma nova linha após o último par chave-valor e
    indente-a em um nível para que esteja alinhada com as chaves do
    dicionário. Incluir uma vírgula após o último par chave-valor também
    é uma boa prática; assim você estará preparado para acrescentar um
    novo par chave-valor na próxima linha.

    A palavra print é menor que a maioria dos nomes de dicionário,
    portanto faz sentido incluir a primeira parte do que você quer
    exibir logo depois do parêntese de abertura. Escolha um ponto
    apropriado para separar o que está sendo exibido e acrescente um
    operador de concatenação ( + ) no final da primeira linha. Tecle
    ENTER e depois TAB para alinhar todas as linhas subsequentes em um
    nível de indentação abaixo da instrução print . Quando terminar de
    compor sua saída, você pode colocar o parêntese de fechamento na
    última linha do bloco print.

    - Percorrendo todos os pares chave-valor com um laço

    O código diz a Python para percorrer todos os pares chave-valor do
    dicionário com um laço. À medida que cada par é tratado, a chave é
    armazenada na variável name e o valor, na variável language. Esses
    nomes descritivos fazem com que seja muito mais fácil ver o que a
    instrução print() faz.

    - Percorrendo todas as chaves de um dicionário com um laço

    A linha for name in favorite_languages.keys() diz a Python para
    extrair todas as chaves do dicionário favorite_languages e
    armazená-las, uma de cada vez, na variável name. A saída mostra os
    nomes de todos que participaram da enquete.

    Percorrer as chaves, na verdade, é o comportamento-padrão quando
    percorremos um dicionário com um laço, portanto este código
    produzirá a mesma saída se escrevêssemos:

    for name in favorite_languages:

    em vez de:

    for name in favorite_languages.keys():

    Você pode optar por usar o método keys() explicitamente se isso
    deixar seu código mais fácil de ler, ou pode omiti-lo, se quiser.

    O método keys() não serve apenas para laços: na verdade, ele devolve
    uma lista de todas as chaves, e simplesmente verifica se 'erin' está
    nessa lista. Como ela não está, uma mensagem é exibida convidando-a
    a participar da enquete.

    - Percorrendo as chaves de um dicionário em ordem usando um laço

    Essa instrução for é como as outras instruções for, exceto que a
    função sorted() está em torno do método dictionary.keys(). Isso diz
    a Python para listar todas as chaves do dicionário e ordenar essa
    lista antes de percorrê-la com um laço. A saída mostra os nomes de
    todos que responderam à enquete, exibidos de forma ordenada.

    - Percorrendo todos os valores de um dicionário com um laço

    A instrução for, nesse caso, extrai cada valor do dicionário e o
    armazena na variável language. Quando esses valores são exibidos,
    temos uma lista de todas as linguagens escolhidas.

    Quando colocamos set() em torno de uma lista que contenha itens
    duplicados, Python identifica os itens únicos na lista e cria um
    conjunto a partir desses itens. Usamos set() para extrair as
    linguagens únicas em favorite_languages.values().

    - FAÇA VOCÊ MESMO:

    6.6 – Enquete: Utilize o código em favorite_languages.py (página
    150).

    • Crie uma lista de pessoas que devam participar da enquete sobre
    linguagem favorita. Inclua alguns nomes que já estejam no
    dicionário e outros que não estão.

    • Percorra a lista de pessoas que devem participar da enquete. Se
    elas já tiverem respondido à enquete, mostre uma mensagem
    agradecendo-lhes por responder. Se ainda não participaram da
    enquete, apresente uma mensagem convidando-as a responder.

------------------------------------------------------------------------

HISTÓRICO
    20202310: João Paulo, outubro de 2020.
        - Um dicionário de objetos semelhantes - Pag. 136-137.

    20202410: João Paulo, outrubro de 2020.
        - Percorrendo todos os pares chave-valor com um laço
        (pg 139-140).
        - Percorrendo todas as chaves de um dicionário com um laço
        (pg 140-141).
        - Percorrendo as chaves de um dicionário em ordem usando um laço
        (pg 141-142).
        - Percorrendo todos os valores de um dicionário com um laço
        (pg 142-143).

    20202610: João Paulo, outubro 202.
        - FAÇA VOCÊ MESMO: 6.6 – Enquete (pg 143-144).

"""


favorite_languages = { 'jen' : 'python',
                       'sarah' : 'c',
                       'edward' : 'ruby',
                       'phil' : 'python',}

# Essa sintaxe é usada na instrução print(), e a saída mostra a
# linguagem predileta de Sarah:
print("\n- Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".\n")

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

print()

for name in favorite_languages.keys():
    print(name.title())

print()

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll!")

print()

# sorted() - organiza a lista
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("\nThe following languages have been mentioned:")

# set() - retira a duplicidade
for language in set(favorite_languages.values()):
    print(language.title())

print()

participantes = ['johnny', 'jot', 'jen', 'sarah',]

for name in favorite_languages.keys():
    if name in participantes:
        print("\n- " + name.title() + " obrigado por responder nossa enquete.")

    else:
        print("\n- " + name.title() + " sua participação é muito importante.")
