from django.urls import path
from . import views


urlpatterns = [
    # Página inicial.
    path('', views.index, name='index'),
]
