#! /usr/bin/env python3

"""
------------------------------------------------------------------------

NOME
    hn_submissions.py - A API de Hacker News.

------------------------------------------------------------------------

SINOPSES
    $ chmod +x hn_sudmissions.py
    $ ./hn_submissions.py
    Status code: 200
    200
    200
    200
    200
    200
    200
    200
    200
    200
    200
    200
    200
    200
    200
    200
    200
    200
    200
    200
    200
    200
    200
    200
    200
    200
    200
    200
    200
    200
    200

    Title: Linus Torvalds' good taste argument for linked lists,
    explained
    Discussion link: http://news.ycombinator.com/item?id=25326552
    Comments: 238

    Title: The Death of Tony Hsieh: A Spiral of Alcohol, Drugs and
    Extreme Behavior
    Discussion link: http://news.ycombinator.com/item?id=25326510
    Comments: 231

    Title: A container ship lost a record 1,800 containers
    Discussion link: http://news.ycombinator.com/item?id=25328741
    Comments: 179

    Title: Every Model Learned by Gradient Descent Is Approximately a
    Kernel Machine
    Discussion link: http://news.ycombinator.com/item?id=25314830
    Comments: 102

    Title: A tool for recovering passwords from pixelized screenshots
    Discussion link: http://news.ycombinator.com/item?id=25326450
    Comments: 101

    Title: Winning back the Internet by building our own
    Discussion link: http://news.ycombinator.com/item?id=25322834
    Comments: 100

    Title: My Procedurally Generated Music Is Awful
    Discussion link: http://news.ycombinator.com/item?id=25327533
    Comments: 83

    Title: Falling Out of Love with Apple, Part 3: Content and
    Censorship
    Discussion link: http://news.ycombinator.com/item?id=25327951
    Comments: 73

    Title: EmacsConf 2020 Talks
    Discussion link: http://news.ycombinator.com/item?id=25324311
    Comments: 63

    Title: Show HN: Boltstream – Self-hosted full end-to-end live video
    streaming platform
    Discussion link: http://news.ycombinator.com/item?id=25328622
    Comments: 56

    Title: A man who posted himself to Australia (2015)
    Discussion link: http://news.ycombinator.com/item?id=25321836
    Comments: 51

    Title: Rewriting LaTeX in Pure Rust
    Discussion link: http://news.ycombinator.com/item?id=25328874
    Comments: 46

    Title: New Sauerbraten 2020 Edition Released
    Discussion link: http://news.ycombinator.com/item?id=25327267
    Comments: 39

    Title: Areweyet
    Discussion link: http://news.ycombinator.com/item?id=25326401
    Comments: 39

    Title: Google removes some IAC browser extensions for 'policy
    violations'
    Discussion link: http://news.ycombinator.com/item?id=25328576
    Comments: 38

    Title: Let’s Encrypt moving to new CA root
    Discussion link: http://news.ycombinator.com/item?id=25327137
    Comments: 29

    Title: Why Programming Is Hard to Fundamentally Improve (2017)
    Discussion link: http://news.ycombinator.com/item?id=25322656
    Comments: 23

    Title: The CIA's Deadly Deceits and the Vietnam War, with Ralph
    McGehee (1986)
    Discussion link: http://news.ycombinator.com/item?id=25329913
    Comments: 21

    Title: From LEGOs to Ziploc: The Science of the Snap Fit
    Discussion link: http://news.ycombinator.com/item?id=25321638
    Comments: 16

    Title: Isaac Newton’s attempts to unlock secret code of pyramids
    Discussion link: http://news.ycombinator.com/item?id=25322741
    Comments: 11

    Title: Sugar – a typed lispy language targeting webasm/wat
    Discussion link: http://news.ycombinator.com/item?id=25322596
    Comments: 10

    Title: Show HN: Squiggle – A Sketch library for making low-fidelity
    wireframes
    Discussion link: http://news.ycombinator.com/item?id=25327808
    Comments: 7

    Title: Show HN: Exophysics – WebGL2 particle simulator
    Discussion link: http://news.ycombinator.com/item?id=25319394
    Comments: 6

    Title: Dangerous Ransomware Technique
    Discussion link: http://news.ycombinator.com/item?id=25322037
    Comments: 6

    Title: The Danish climate minister closing down the oil industry for good
    Discussion link: http://news.ycombinator.com/item?id=25330581
    Comments: 3

    Title: A technique from human archaeology could help restore sea
    otter populations
    Discussion link: http://news.ycombinator.com/item?id=25320954
    Comments: 2

    Title: Understanding the role of individual units in a deep neural
    network
    Discussion link: http://news.ycombinator.com/item?id=25323360
    Comments: 0

    Title: Self-Driving Cars with Duckietown: Learning Autonomy on the Jetson Nano
    Discussion link: http://news.ycombinator.com/item?id=25323435
    Comments: 0

    Title: WW1 trench fever identified in former homeless man in Canada
    Discussion link: http://news.ycombinator.com/item?id=25330774
    Comments: 0

    Title: The Muse (YC W12) Is Hiring a Director of Account Management
    Discussion link: http://news.ycombinator.com/item?id=25326590
    Comments: 0

------------------------------------------------------------------------

DESCRIÇÃO
    Inicialmente fizemos a chamada de API e exibimos o status da
    resposta.

    Essa chamada de API devolve uma lista contendo os IDs dos 500
    artigos mais populares do Hacker News no momento em que a chamada
    foi feita. Então convertemos o texto da resposta em uma lista
    Python, que armazenamos em submission_ids. Usaremos esses IDs para
    criar um conjunto de dicionários em que cada um armazenará
    informações sobre um dos artigos submetidos.

    Criamos uma lista vazia chamada submission_dicts para armazenar
    esses dicionários. Então percorremos os IDs dos 30 principais
    artigos submetidos com um laço. Fazemos uma nova chamada de API para
    cada artigo gerando um URL que inclui o valor atual de
    submission_id. Exibimos o status de cada requisição para que
    possamos ver se ela foi bem-sucedida.

    Criamos um dicionário para o artigo submetido processado no momento,
    no qual armazenamos o título do artigo e um link para a página de
    discussão desse item. Armazenamos o número de comentários no
    dicionário. Se um artigo ainda não teve nenhum comentário, a chave
    'descendants' não estará presente. Quando você não tiver certeza de
    que uma chave existe em um dicionário, utilize o método dict.get(),
    que devolve o valor associado à chave especificada se ela existir,
    ou o valor que você fornecer se ela não existir (0 nesse exemplo).

    Por fim, concatenamos cada submission_dict à lista submission_dicts.
    
    Os artigos submetidos no Hacker News são classificados de acordo com
    uma pontuação geral, baseada em vários fatores, incluindo quantos
    votos receberam, quantos comentários foram feitos e quão
    recentemente o artigo foi submetido. Queremos ordenar a lista de
    dicionários de acordo com o número de comentários. Para isso, usamos
    uma função chamada itemgetter(), proveniente do módulo operator.

    Passamos a chave 'comments' a essa função e ela extrai o valor
    associado a essa chave de cada dicionário da lista. A função
    sorted() então utiliza esse valor como base para ordenar a lista.

    Ordenamos a lista na ordem inversa para colocar as histórias mais
    comentadas antes.

    Depois que a lista estiver ordenada, nós a percorremos com um laço e
    exibimos três informações sobre cada um dos principais artigos
    submetidos: o título, um link para a página de discussão e o número
    de comentários que o artigo submetido tem no momento.

------------------------------------------------------------------------

HISTÓRICO
    20200712: João Paulo, dezembro de 2020.
        - A API de Hacker News (pg 436-439).

------------------------------------------------------------------------
"""


import requests

from operator import itemgetter


# Faz uma chamada de API e armazena a resposta 
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'

r = requests.get(url)
print("Status code:", r.status_code)

# Processa informações sobre cada artigo submetido
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]: 
    # Cria uma chamada de API separada para cada artigo submetido
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) +
            '.json')
    
    submission_r = requests.get(url)
    print(submission_r.status_code)

    response_dict = submission_r.json() 
    submission_dict = {'title': response_dict['title'],
            'link': 'http://news.ycombinator.com/item?id=' +
            str(submission_id), 'comments': response_dict.get('descendants', 0) }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
            reverse=True)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])
