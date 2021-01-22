"""
20210501: João Paulo, janeiro de 2021.
- Função de view edit_entry() (pg 487):
    Inicialmente devemos importar o modelo Entry.

    Adquirimos o objeto da entrada que o usuário quer editar e o assunto
    associado a essa entrada.
    No bloco if, executado para uma requisição GET, criamos uma
    instância de EntryForm com o argumento instance=entry.

    Esse argumento diz a Django para criar o formulário previamente
    preenchido com informações do objeto de entrada existente.

    O usuário verá os dados existentes e poderá editá-los.

    Ao processar uma requisição POST, passamos os argumentos
    instance=entry e data=request.POST para dizer a Django que crie uma
    instância de formulário baseada nas informações associadas ao objeto
    de entrada existente, atualizadas com qualquer dado relevante de
    request.POST.

    Então verificamos se o formulário é válido; em caso afirmativo,
    chamamos save() sem argumentos.

    Em seguida redirecionamos o usuário para a página topic, na qual ele
    deverá ver a versão atualizada da entrada editada.

------------------------------------------------------------------------

    Inicialmente importamos o modelo associado aos dados de que
    precisamos.

    A função topics() exige um parâmetro: o objeto request que Django
    recebeu do servidor.

    Consultamos o banco de dados pedindo os objetos Topic, ordenados de
    acordo com o atributo date_added.

    Armazenamos o queryset resultante em topics.

    Definimos um contexto que será enviado ao template.

    Um contexto é um dicionário em que as chaves são os nomes que
    usaremos no template para acessar os dados e os valores são os dados
    que devemos enviar ao template.

    Nesse caso, há apenas um par chave-valor, que contém o conjunto de
    assuntos a ser exibido na página.

    Ao construir uma página que use dados, passamos a variável context
    para render(), além do objeto request e o path do template.

------------------------------------------------------------------------

def topic(request, topic_id):

    Essa é a primeira função de view que exige um parâmetro que não seja
    o objeto request.

    A função aceita o valor capturado pela expressão (?P<topic_id>\d+),
    atualizado para o django 3.1.4, e o armazena em topic_id.

    Usamos get() para obter o assunto, assim como fizemos no shell de
    Django.

    Recuperamos as entradas associadas aesse assunto e as ordenamos de
    acordo com date_added: o sinal de menos na frente de date_added
    ordena os resultados em ordem inversa, o que fará as entradas mais
    recentes serem exibidas antes.

    Armazenamos o assunto e as entradas no dicionário de contexto e
    enviamos context para o template topic.html.

------------------------------------------------------------------------

    Importamos a classe HttpResponseRedirect, que usaremos para
    redirecionar o leitor de volta à página topics, depois que ele tiver
    submetido o seu assunto.

    A função reverse() determina o URL a partir de um padrão de URL
    nomeado, o que quer dizer que Django gerará o URL quando a página
    for solicitada.

    Também importamos TopicForm, que é o formulário que acabamos de
    criar.

------------------------------------------------------------------------

    A função new_topic() aceita o objeto de requisição como parâmetro.

    Quando o usuário inicialmente solicita essa página, o navegador
    envia uma requisição GET.

    Depois que o usuário tiver preenchido e submetido o formulário, o
    navegador enviará uma requisição POST.

    Conforme a requisição, saberemos se o usuário está solicitando um
    formulário em branco (uma requisição GET) ou nos pedindo para
    processar um formulário preenchido (uma requisição POST).

    O teste determina se o método de requisição é GET ou POST.

    Se o método de requisição não for um POST, a requisição
    provavelmente é um GET, portanto precisamos devolver um formulário
    em branco (se for outro tipo de requisição, continua sendo seguro
    devolver um formulário em branco).

    Criamos uma instância de TopicForm, armazenamos essa instância em
    uma variável form e enviamos o formulário para o template no
    dicionário de contexto.

    Como não incluímos nenhum argumento ao instanciar TopicForm, o
    Django cria um formulário em branco que o usuário poderá preencher.

    Se o método de requisição for um POST, o bloco else executará e
    processará os dados submetidos no formulário.

    Criamos uma instância de TopicForm e passamos os dados fornecidos
    pelo usuário, armazenados em request.POST.

    O objeto form devolvido contém as informações submetidas pelo
    usuário.

    Não podemos salvar as informações submetidas no banco de dados antes
    de verificar se são válidas.

    A função is_valid() verifica se todos os campos necessários foram
    preenchidos (todos os campos em um formulário são obrigatórios por
    padrão) e se os dados fornecidos são do tipo esperado para o campo –
    por exemplo, se o tamanho de text é menor que 200 caracteres,
    conforme especificado em models.py no Capítulo 18.

    Essa validação automática nos poupa de muito trabalho.

    Se tudo estiver válido, chamamos save(), que grava os dados do
    formulário no banco de dados.

    Depois que os dados forem salvos, podemos sair dessa página.

    Usamos reverse() para obter o URL da página topics e o passamos para
    HttpResponseRedirect(), que redireciona o navegador do usuário para
    essa página.

    Na página topics, o usuário deverá ver o assunto que ele acabou de
    inserir na lista de assuntos.

------------------------------------------------------------------------

    Atualizamos a instrução import para incluir o EntryForm que acabamos
    de criar.

    A definição de new_entry() tem um parâmetro topic_id para armazenar
    o valor recebido do URL.

    Precisaremos do assunto para renderizar a página e processar os
    dados do formulário, portanto utilizamos topic_id para obter o
    objeto correto para o assunto.

    Verificamos se o método de requisição é POST ou GET.

    O bloco if executará se for uma requisição GET, e criaremos uma
    instância em branco de EntryForm.

    Se o método de requisição for um POST, processaremos os dados
    criando uma instância de EntryForm, preenchida com os dados de POST
    do objeto request.

    Então verificamos se o formulário é válido.

    Se for, devemos definir o atributo topic do objeto de entrada antes
    de salvá-lo no banco de dados.

    Quando chamamos save(), incluímos o argumento commit=False para
    dizer a Django que crie um novo objeto de entrada e o armazene em
    new_entry sem salvá-lo no banco de dados por enquanto.

    Definimos o atributo topic de new_entry com o assunto extraído do
    banco de dados no início da função; então chamamos save() sem
    argumentos.

    Essa instrução salva a entrada no banco de dados com o assunto
    correto associado.

    Redirecionamos o usuário para a página do assunto.

    A chamada a reverse() exige dois argumentos: o nome do padrão de URL
    para o qual queremos gerar um URL e uma lista args contendo qualquer
    argumento que deva ser incluído no URL.

    A lista args contém um item: topic_id. A chamada a
    HttpResponseRedirect() então redireciona o usuário para a página do
    assunto para o qual uma entrada foi criada, e a nova entrada deverá
    ser vista na lista de entradas.

20212201: João Paulo, janeiro de 2021.
- Restringindo o acesso à página de assuntos (pg 489-499):
    Inicialmente importamos a função login_required(). Aplicamos
    login_required() como um decorador da função de view topics()
    prefixando login_required com o símbolo @ para que Python saiba que
    deve executar o código em login_required() antes do código em
    topics(). O código em login_required() verifica se um usuário está
    logado, e Django executará o código em topics() somente em caso
    afirmativo. Se não estiver logado, o usuário será redirecionado para
    a página de login.
"""


from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.urls import reverse
from django.contrib.auth.decorators import login_required

from . models import Topic, Entry
from . forms import TopicForm, EntryForm


def index(request):
    """A página inicial de Learning Log."""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """Mostra todos os assuntos."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Mostra um único assunto e todas as suas entradas."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Adiciona um novo assunto."""
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = TopicForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = TopicForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """Acrescenta uma nova entrada para um assunto em particular."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = EntryForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, entry_id):
    """Edita uma entrada existente."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Requisição inicial;
        # preenche previamente o formulário com a entrada atual.
        form = EntryForm(instance=entry)
    else:
        # Dados de POST submetidos; processa os dados.
        form = EntryForm(instance=entry, data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
