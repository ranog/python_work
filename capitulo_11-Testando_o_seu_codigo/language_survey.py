#! /usr/bin/env python3

"""
------------------------------------------------------------------------

NOME
    language_survey.py - Uma classe para testar.

------------------------------------------------------------------------
SINOPSES
    $ chmod +x language_survey.py
    $ ./language_survey.py
    What language did you first learn to speak?
    Enter 'q' at any time to quit.

    Language: English
    Language: Spanish
    Language: English
    Language: Mandarin
    Language: q

    Thank you to everyone who participated in the survey!
    Survey results:
    - English
    - Spanish
    - English
    - Mandarin

------------------------------------------------------------------------

DESCRIÇÃO
    - Uma classe para testar:
        Esse programa define uma pergunta ("What language did you first
        learn to speak?", ou seja, “Qual foi a primeira língua que você
        aprendeu a falar?”) e cria um objeto AnonymousSurvey com essa
        pergunta. O programa chama show_question() para exibir a
        pergunta e então espera as respostas. Cada resposta é armazenada
        à medida que é recebida. Quando todas as respostas tiverem sido
        fornecidas (o usuário digitou q para sair), show_results()
        exibirá o resultado da pesquisa.

        Essa classe funciona para uma pesquisa anônima simples.

------------------------------------------------------------------------

HISTÓRICO
    20202911: João Paulo, novembro de 2020.
        - Uma classe para testar (pg 265-266).

------------------------------------------------------------------------

"""


from survey import AnonymousSurvey

# Define uma pergunta e cria uma pesquisa
question = "What language did you first learn to speak? "
my_survey = AnonymousSurvey(question)

# Mostra a pergunta e armazena as respostas à pergunta
my_survey.show_question()

print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response.lower() == 'q':
        break
    my_survey.store_response(response)

# Exibe os resultados da pesquisa
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
