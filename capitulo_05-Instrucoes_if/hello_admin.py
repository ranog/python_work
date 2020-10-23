#! /usr/bin/env python3

"""
NOME
    toppings.py - Verificando a diferença

SINOPSES
    chmod +x toppings.py
    ./toppings.py
    Hold the anchovies!
    True
    False

DESCRIÇÃO
    Compara o valor de requested_topping com o valor 'anchovies'. Se esses dois
    valores não forem iguais, Python devolverá True e executará o código após a
    instrução if. Se esses dois valores forem iguais, Python devolverá  False e
    não executará o código após essa instrução.

    A palavra reservada in diz a Python para verificar a existência de 'mushrooms'
    e de 'pepperoni' na lista requested_toppings.

    - Testando várias condições

    Começamos com uma lista contendo os ingredientes solicitados. A instrução
    if verifica se a pessoa pediu cogumelos ('mushrooms') em sua pizza. Em caso
    afirmativo, uma mensagem será exibida para confirmar esse ingrediente. O
    teste para pepperoni corresponde a outra instrução if simples, e não a uma
    instrução elif ou else, portanto esse teste é executado independentemente
    de o teste anterior ter passado ou não. O código verifica se queijo extra
    ('extra cheese') foi pedido, não importando o resultado dos dois primeiros
    testes. Esses três testes independentes são realizados sempre que o programa
    é executado.


    - Verificando itens especiais

    O código verifica se a pessoa pediu pimentões verdes. Em caso afirmativo,
    exibimos uma mensagem informando por que ela não pode ter pimentões verdes.
    O bloco else garante que todos os demais ingredientes serão adicionados à
    pizza.

    - Verificando se uma lista não está vazia

    Dessa vez, começamos com uma lista vazia de ingredientes. Em vez de passar
    diretamente para um laço for, fazemos uma verificação rápida. Quando o nome
    de uma lista é usado em uma instrução if, Python devolve True se a lista
    contiver pelo menos um item; uma lista vazia é avaliada como False. Se
    requested_toppings passar no teste condicional, executamos o mesmo laço for
    do exemplo anterior. Se o teste condicional falhar, exibimos uma mensagem
    perguntando ao cliente se ele realmente quer uma pizza simples, sem
    ingredientes adicionais.


    - Usando várias listas

    Definimos uma lista de ingredientes disponíveis nessa pizzaria. Observe que
    essa informação poderia ser uma tupla se a pizzaria tiver uma seleção estável
    de ingredientes. Criamos uma lista de ingredientes solicitados por um cliente.
    Observe a solicitação incomum, 'french fries' (batatas fritas). Percorremos
    a lista de ingredientes solicitados em um laço. Nesse laço, inicialmente
    verificamos se cada ingrediente solicitado está na lista de ingredientes
    disponíveis. Se estiver, adicionamos esse ingrediente na pizza. Se o
    ingrediente solicitado não estiver na lista de ingredientes disponíveis, o
    bloco else será executado. Esse bloco exibe uma mensagem informando ao
    usuário quais ingredientes não estão disponíveis.

----------------------------------------------------------------------

HISTÓRICO
    20202110: João Paulo, outubro de 2020.
        - Implementação da função para determinar se dois valores não são
        iguais;
        - Verificando se um valor está em uma lista;
        - Testando várias condições - Pag. 121;

    20202210: João Paulo, outubro de 2020.
        - Verificando itens especiais - Pag. 124-125;
        - Verificando se uma lista não está vazia - Pag. 125-126;
        - Usando várias listas - Pag. 126-127.

"""


requested_topping = ['mushrooms']

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

requested_toppings = ['mushrooms', 'onions', 'pineapple','extra cheese']

print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

if 'mushrooms' in requested_toppings: print("\n- Adding mushrooms.")
if 'pepperoni' in requested_toppings: print("\n- Adding pepperoni.")
if 'extra cheese' in requested_toppings: print("\n- Adding extra cheese")

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("\n- Sorry, we are out of " + requested_topping + " right now.")
    else: print("\n- Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("\n- Sorry, we are out of " + requested_topping + " right now.")
        else: print("\n- Adding " + requested_topping + ".")

    print("\n- Finished making your pizza!")

else:print("\n- Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("\n- Adding " + requested_topping + ".")
    else: print("\n- Sorry, we don't have " + requested_topping + ".")

print("\n- Finished making your pizza!")
