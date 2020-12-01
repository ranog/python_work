#! /usr/bin/env python3

"""
------------------------------------------------------------------------

NOME
    python_repos.py - Processando uma resposta de AP.

------------------------------------------------------------------------

SINOPSES
    $ chmod +x python_repos.py
    $ ./python_repos.py

------------------------------------------------------------------------

DESCRIÇÃO
    Importamos o módulo requests. Armazenamos o URL da chamada da API e
    então usamos requests para fazer a chamada. Chamamos get(),
    passamos o URL e armazenamos o objeto com a resposta na variável
    r. O objeto com a resposta tem um atributo chamado status_code, que
    nos informa se a requisição foi bem-sucedida. (Um código de status
    igual a 200 indica sucesso na resposta.) Exibimos o valor de
    status_code para garantir que a chamada foi realizada com sucesso.

    A API devolve as informações em formato JSON, portanto usamos o
    método json() para convertê-las em um dicionário Python.
    Armazenamos o dicionário resultante em response_dict.
    Por fim, exibimos as chaves de response_dict.

 
# XXX tenho que arrumar isso:
 : Status
code: 200
dict_keys(['items', 'total_count', 'incomplete_results']) Como o código
de status é 200, sabemos que a requisição teve sucesso. O dicionário com
a resposta contém apenas três chaves: 'items', 'total_count' e
'incomplete_results'.
NOTA Chamadas simples como essa devem devolver um conjunto completo
de resultados, portanto é seguro ignorar o valor associado a
'incomplete_results'. Porém, quando fizer chamadas de API mais
complexas, seu programa deverá conferir esse valor.
------------------------------------------------------------------------

HISTÓRICO
    20200112: João Paulo, dezembro de 2020.
        - Processando uma resposta de AP (pg 425-426).

------------------------------------------------------------------------
"""


import requests

# Faz uma chamada de API e armazena a resposta.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print("Status code: ", r.status_code)

# Armazena a resposta da API em uma variável
response_dict = r.json()

# Processa o resultado
print(response_dict.keys())
