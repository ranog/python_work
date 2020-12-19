"""Define padrões de URL para Pizzas."""

from django.urls import path
from . import views


urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),
    path('pizzas/', views.pizzas, name='pizzas'),
    # Página dos ingredientes de um pizza.
    path('pizzas/<int:pizza_id>', views.pizza, name='pizza'),
]
