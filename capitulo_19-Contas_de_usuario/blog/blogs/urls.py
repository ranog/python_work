"""
    Define padrões de URL para learning_logs.
"""

from django.urls import path
from . import views


urlpatterns = [
    # Página inicial.
    path('', views.index, name='index'),

    # Página para adicionar um novo post.
    path('new_post/', views.new_post, name='new_post'),

    # Página para editar um post.
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]
