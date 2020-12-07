#! /usr/bin/env python3

"""
------------------------------------------------------------------------

NOME
    outras_linguagens.py - FAÇA VOCÊ MESMO.

------------------------------------------------------------------------

SINOPSES
    $ chmod +x outras_linguagens.py
    $ ./outras_libguagens.py

------------------------------------------------------------------------

DESCRIÇÃO
    17.1 – Outras linguagens: Modifique a chamada de API em
    python_repos.py para que ela gere um gráfico mostrando os projetos
    mais populares em outras linguagens. Experimente usar linguagens
    como JavaScript, Ruby, C, Java, Perl, Haskell e Go.

------------------------------------------------------------------------

HISTÓRICO
    20200712: João Paulo, dezembro de 2020.
        - 17.1 – Outras linguagens (pg 439).

------------------------------------------------------------------------
"""


import requests
import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# Faz uma chamada de API e armazena a resposta.

linguagens = ['javascript', 'ruby', 'c', 'java', 'perl']

for linguagem in linguagens:

    url = 'https://api.github.com/search/repositories?q=language:' + linguagem + '&sort=stars'

    r = requests.get(url)
    print("Status code:", r.status_code)

    # Armazena a resposta da API em uma variável
    response_dict = r.json()

    print("Total repositories:", response_dict['total_count'])

    # Explora informações sobre os repositórios
    repo_dicts = response_dict['items']

    names, plot_dicts = [], []

    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])

        plot_dict = {'value': repo_dict['stargazers_count'],
                 'label': repo_dict['description'],
                 'xlink': repo_dict['html_url'],}
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
    chart.title = 'Most-Starred ' + linguagem + ' Projects on GitHub'
    chart.x_labels = names

    chart.add('', plot_dicts)

    arquivo = linguagem + '_repos.svg'
    chart.render_to_file(arquivo)
