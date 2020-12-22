from django.shortcuts import render
from django.http import HttpResponseRedirect 

# Livro: from django.core.urlresolvers import reverse
from django.urls import reverse

from . models import Topic
from . forms import TopicForm

# Create your views here.
""" Inicialmente importamos o modelo associado aos dados de que
precisamos.

A função topics() exige um parâmetro: o objeto request que Django
recebeu do servidor.

Consultamos o banco de dados pedindo os objetos Topic, ordenados de
acordo com o atributo date_added.

Armazenamos o queryset resultante em topics.

Definimos um contexto que será enviado ao template.

Um contexto é um dicionário em que as chaves são os nomes que usaremos
no template para acessar os dados e os valores são os dados que devemos
enviar ao template.

Nesse caso, há apenas um par chave-valor, que contém o conjunto de
assuntos a ser exibido na página.

Ao construir uma página que use dados, passamos a variável context para
render(), além do objeto request e o path do template.

------------------------------------------------------------------------

def topic(request, topic_idid

    Essa é a primeira função de view que exige um parâmetro que não seja
    o objeto request.

    A função aceita o valor capturado pela expressão (?P<topic_id>\d+),
    atualizado para o django 3.1.4, e o armazena em topic_id.

    Usamos get() para obter o assunto, assim como fizemos no shell de Django.
    
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
    inserir na lista de assuntos. """


def index(request):
    """A página inicial de Learning Log."""
    return render(request, 'learning_logs/index.html')


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
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
