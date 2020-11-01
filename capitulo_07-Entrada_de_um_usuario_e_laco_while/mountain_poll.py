#! /usr/bin/env python3

"""
NOME
    mountain_poll.py -Preenchendo um dicionário com dados de entrada do
    usuário.

SINOPSES
    chmod +x mountain_poll.py
    ./mountain_poll.py

    - Preenchendo um dicionário com dados de entrada do usuário:

    What is your name? eric
    Which mountain would you like to climb someday? denali
    Would you like to let another person respond? (yes / no) yes

    What is your name? Lynn
    Which mountain would you like to climb someday? devil's thumb
    Would you like to let another person respond? (yes / no) no

    --- Poll Results ---
    Eric would like to climb Denali.
    Lynn would like to climb Devil'S Thumb.

DESCRIÇÃO
    O programa inicialmente define um dicionário vazio (responses) e
    cria uma flag (polling_active) para indicar que a enquete está
    ativa. Enquanto polling_active for True, Python executará o código
    que está no laço while. Nesse laço é solicitado ao usuário que entre
    com seu nome e uma montanha que gostaria de escalar. Essa informação
    é armazenada no dicionário responses, e uma pergunta é feita ao
    usuário para saber se ele quer que a enquete continue. Se o usuário
    responder yes, o programa entrará no laço while novamente. Se
    responder no, a flag polling_active será definida com False, o laço
    while para de executar e o último bloco de código exibe o resultado
    da enquete.

HISTÓRICO
    20200111: João Paulo, outubro de 2020.
        - Preenchendo um dicionário com dados de entrada do usuário (pg
        165-166).

"""


print("\n- Preenchendo um dicionário com dados de entrada do usuário:")

responses = {}

# Define uma flag para indicar que a enquete está ativa
polling_active = True

while polling_active:
    # Pede o nome da pessoa e a resposta
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Armazena a resposta no dicionário
    responses[name] = response

    # Descobre se outra pessoa vai responder à enquete
    repeat = input("Would you like to let another person respond? (yes / no) ")
    if repeat.lower() == 'no':
        polling_active = False

# A enquete foi concluída. Mostra os resultados
print("\n--- Poll Results ---")

for name, response in responses.items():
    print(name.title() + " would like to climb " + response.title() + ".")
