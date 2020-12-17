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
render(), além do objeto request e o path do template."""


def index(request):
    """A página inicial de Learning Log."""
    return render(request, 'learning_logs/index.html')


def topics(resquest):
    """Mostra todos os assuntos."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
