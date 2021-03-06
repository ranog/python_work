"""
    Define padrões de URL para learning_logs.

    Esse padrão de URL corresponde a qualquer URL no formato
    http://localhost:8000/new_entry/id/, em que id é o número de ID de
    um assunto.

    O código (?P<topic_id>\d+) captura um valor numérico e o armazena na
    variável topic_id.

    Quando um URL correspondente a esse padrão for solicitado, o Django
    enviará a requisição e o ID do assunto para a função de view
    new_entry().

20210501: João Paulo, janeiro de 2021.
    - URL edit_entry (pg 486-487):
        O ID passado no URL (por exemplo,
        http://localhost:8000/edit_entry/1/) é armazenado no parâmetro
        entry_id.

        O padrão de URL envia requisições que correspondam a esse
        formato para a função de view edit_entry().

"""

from django.urls import path
from . import views


urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),

    path('topics/', views.topics, name='topics'),

    # Página de detalhes para um único assunto
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Página para adicionar um novo assunto.
    path('new_topic/', views.new_topic, name='new_topic'),

    # Página para adicionar uma nova entrada.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'), 

    # Página para editar uma entrada.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
