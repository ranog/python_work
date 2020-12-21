"""Define padrões de URL para learning_logs."""

from django.urls import path
from . import views


urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),
    
    path('topics/', views.topics, name='topics'),

    # Página de detalhes para um único assunto
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Página para adicionar um novo assunto
    path('new_topic/', views.new_topic, name='new_topic'),
]
