#! /usr/bin/env python3

"""
------------------------------------------------------------------------

NOME
    python_repos.py - Processando uma resposta de AP.

------------------------------------------------------------------------

SINOPSES
    $ chmod +x python_repos.py
    $ ./python_repos.py
    Status code: 200
    dict_keys(['items', 'total_count', 'incomplete_results'])
       
------------------------------------------------------------------------

    Status code: 200
    Total repositories: 6305414
    Repositories returned: 30

    Keys = 74
    archive_url
    archived
    assignees_url
    blobs_url
    branches_url
    clone_url
    collaborators_url
    comments_url
    commits_url
    compare_url
    contents_url
    contributors_url
    created_at
    default_branch
    deployments_url
    description
    disabled
    downloads_url
    events_url
    fork
    forks
    forks_count
    forks_url
    full_name
    git_commits_url
    git_refs_url
    git_tags_url
    git_url
    has_downloads
    has_issues
    has_pages
    has_projects
    has_wiki
    homepage
    hooks_url
    html_url
    id
    issue_comment_url
    issue_events_url
    issues_url
    keys_url
    labels_url
    language
    languages_url
    license
    merges_url
    milestones_url
    mirror_url
    name
    node_id
    notifications_url
    open_issues
    open_issues_count
    owner
    private
    pulls_url
    pushed_at
    releases_url
    score
    size
    ssh_url
    stargazers_count
    stargazers_url
    statuses_url
    subscribers_url
    subscription_url
    svn_url
    tags_url
    teams_url
    trees_url
    updated_at
    url
    watchers
    watchers_count

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

    Como o código de status é 200, sabemos que a requisição teve sucesso. 
    O dicionário com a resposta contém apenas três chaves: 'items', 
    'total_count' e 'incomplete_results'. 
    
    NOTA 
        Chamadas simples como essa devem devolver um conjunto completo
        de resultados, portanto é seguro ignorar o valor associado a
        'incomplete_results'. Porém, quando fizer chamadas de API mais
        complexas, seu programa deverá conferir esse valor.
        
------------------------------------------------------------------------

    Exibimos o valor associado a 'total_count', que representa o número
    total de repositórios Python no GitHub.
    O valor associado a 'items' é uma lista que contém vários
    dicionários, cada um contendo dados sobre um repositório Python
    individual. Armazenamos essa lista de dicionários em repo_dicuiA
    Então exibimos o tamanho de repo_dicts para ver o número de
    repositórios para os quais temos informações.
    Para observar melhor as informações devolvidas sobre cada
    repositório, extraímos o primeiro item de repo_dicts e o armazenamos
    em repo_dict. Então exibimos a quantidade de chaves do dicionário
    para ver quantas informações temyyp
    Exibimos todas as chayyp (keys) do dicionário para ver quais tipos
    de informação estão incluídos.
    O resultado começa a nos dar uma imagem mais clara dos dados
    propriamente ditos.

    A API do GitHub devolve muitas informações sobre cada repositório:
    há 74 chaves em repo_dict. Ao observar essas chaves, você terá uma
    noção do tipo de informação que pode ser extraído a respeito de um
    projeto. (A única maneira de saber quais informações estão
    disponíveis por meio de uma API é ler a documentação ou analisar as
    informações por meio de código, como estamos fazendo nesse caso.).

------------------------------------------------------------------------

HISTÓRICO
    20200112: João Paulo, dezembro de 2020.
        - Processando uma resposta de AP (pg 425-426).
    

    20200212: João Paulo, dezembro de 2020.
        - Trabalhando como dicionário deresposta (pg 426-428).

------------------------------------------------------------------------
"""


import requests

# Faz uma chamada de API e armazena a resposta.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print("Status code:", r.status_code)

# Armazena a resposta da API em uma variável
response_dict = r.json()

# Processa o resultado
# print(response_dict.keys()) pg: 425-426
print("Total repositories:", response_dict['total_count'])

# Explora informações sobre os repositórios
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# Analisa o 1° repositório
repo_dict = repo_dicts[0]
print("\nKeys =", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

# pg 428: print("\nSelected information about first repository:")
