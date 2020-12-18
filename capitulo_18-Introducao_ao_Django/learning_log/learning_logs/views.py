from django.shortcuts import render
from . models import Topic

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
    enviamos context para o template topic.html."""


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
