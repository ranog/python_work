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

    Selected information about first repository:
    Name: system-design-primer
    Owner: donnemartin
    Stars: 113811
    Repository: https://github.com/donnemartin/system-design-primer
    Created: 2017-02-26T16:15:28Z
    Updated: 2020-12-02T20:14:33Z
    Description: Learn how to design large-scale systems. Prep for the
    system design interview.  Includes Anki flashcards.
    ...

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
    individual. Armazenamos essa lista de dicionários em repo_dicts.
    Então exibimos o tamanho de repo_dicts para ver o número de
    repositórios para os quais temos informações.
    Para observar melhor as informações devolvidas sobre cada
    repositório, extraímos o primeiro item de repo_dicts e o armazenamos
    em repo_dict. Então exibimos a quantidade de chaves do dicionário
    para ver quantas informações temos.
    Exibimos todas as chaves (keys) do dicionário para ver quais tipos
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

    Nesse exemplo exibimos os valores de diversas chaves do dicionário
    do primeiro repositório. Exibimos o nome do projeto. Um dicionário
    completo representa o dono do projeto; assim usamos a chave owner
    para acessar o dicionário que o representa e então usamos a chave
    login para obter o seu nome de login. Exibimos a quantidade de
    estrelas que o projeto recebeu e o URL do repositório do projeto no
    GitHub. Em seguida, mostramos a data em que o projeto foi criado e
    quando foi atualizado pela última vez. Por fim, exibimos a descrição
    do repositório.

------------------------------------------------------------------------

    Exibimos uma mensagem introdutória. Percorremos todos os dicionários
    em repo_dicts com um laço.

------------------------------------------------------------------------

    Começamos importando o pygal e os estilos do Pygal de que
    precisaremos para o gráfico. Continuamos exibindo o status da
    resposta da chamada à API e o número total de repositórios
    encontrados para que possamos saber caso haja algum problema com a
    chamada da API. Não exibimos mais as informações sobre os projetos
    específicos devolvidos, pois elas serão incluídas na visualização.
    Criamos duas listas vazias para armazenar os dados que incluiremos
    no gráfico. Precisaremos do nome de cada projeto para rotular as
    barras e do número de estrelas para determinar a altura delas. No
    laço, concatenamos nessas listas o nome de cada projeto e o número
    de estrelas que ele tem. Em seguida, definimos um estilo usando a
    classe LightenStyle (alias LS) e usamos um tom de azul-escuro como
    base. Também passamos o argumento base_style para utilizar a classe
    LightColorizedStyle (alias LCS).
    Então usamos Bar() para criar um gráfico de barras simples e lhe
    passamos my_style. Além disso, passamos outros dois argumentos de
    estilo: definimos a rotação dos nomes ao longo do eixo x em 45 graus
    (x_label_rotation=45) e ocultamos a legenda, pois estamos plotando
    apenas uma série no gráfico (show_legend=False). Então fornecemos um
    título ao gráfico e definimos o atributo x_labels com a lista names.
    Como não é necessário nomear essa série de dados, passamos uma
    string vazia para o rótulo quando adicionamos os dados. 

------------------------------------------------------------------------

    Criamos uma instância chamada my_config da classe Config do Pygal;
    modificar os atributos de my_config personalizará a aparência do
    gráfico.

    Definimos os dois atributos x_label_rotation e show_legend,
    originalmente passados como argumentos nomeados quando criamos uma
    instância de Bar. Definimos o tamanho da fonte para o título do
    gráfico e para os rótulos menores e maiores. Os rótulos menores
    nesse gráfico são os nomes dos projetos ao longo do eixo x e a maior
    parte dos números no eixo y. Os rótulos maiores são apenas os
    rótulos do eixo y que marcam incrementos de 5.000 estrelas. Esses
    rótulos serão maiores, e é por isso que os diferenciamos. Usamos
    truncate_label para reduzir os nomes de projeto mais longos a 15
    caracteres. (Quando você passar o mouse sobre um nome de projeto
    truncado na tela, o nome completo aparecerá.) Em seguida, ocultamos
    as linhas horizontais do gráfico definindo show_y_guides com False.
    Por fim, definimos uma largura personalizada para que o gráfico use
    mais do espaço disponível no navegador.

    Agora, quando criamos uma instância de Bar(), passamos my_config
    como primeiro argumento, e todas as nossas definições de
    configuração serão enviadas em um só argumento. Podemos fazer
    quantas modificações de estilo e de configuração quisermos por meio
    de my_config. 

------------------------------------------------------------------------

HISTÓRICO
    20200112: João Paulo, dezembro de 2020.
        - Processando uma resposta de AP (pg 425-426).
    

    20200212: João Paulo, dezembro de 2020.
        - Trabalhando como dicionário deresposta (pg 426-428).

    20200312: João Paulo, dezembro de 2020.
        - Resumo dos principais repositórios (pg 428-429).
        - Visualizando os repositórios usando o Pygal (pg 430-432).

    20200412: João Paulo, dezembro de 2020.
        - Aperfeiçoando os gráficos do Pygal (pg 432-433).
        
    20200412: João Paulo, dezembro de 2020.
        - Plotando os dados (pg 435).

------------------------------------------------------------------------
"""


import requests
import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# Faz uma chamada de API e armazena a resposta.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print("Status code:", r.status_code)

# Armazena a resposta da API em uma variável
response_dict = r.json()

#-----------------------------------------------------------------------

# Processa o resultado
# print(response_dict.keys()) pg: 425-426

#-----------------------------------------------------------------------

print("Total repositories:", response_dict['total_count'])

# Explora informações sobre os repositórios
repo_dicts = response_dict['items']
print("Number of items:", len(repo_dicts))

names, plot_dicts = [], []



#-----------------------------------------------------------------------

"""# Analisa o 1° repositório
repo_dict = repo_dicts[0]
print("\nKeys =", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)"""

#-----------------------------------------------------------------------

"""
print("\nSelected information about each repository:")

for repo_dict in repo_dicts:
    print('Name:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])
    print()"""

#-----------------------------------------------------------------------

names, stars = [], []

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
#    stars.append(repo_dict['stargazers_count']) - exemplo anterior
    plot_dict = {'value' : repo_dict['stargazers_count'],
            'label' : repo_dict['description'],}
    plot_dicts.append(plot_dict)
   
    # Cria uma visualização
    my_style = LS('#333366', base_style=LCS)
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size = 18
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000

    chart = pygal.Bar(my_config, style=my_style)
    chart.title = 'Most-Starred Python Projects on GitHub'
    chart.x_labels = names
    chart.add('', plot_dicts) 
    chart.render_to_file('python_repos.svg')
