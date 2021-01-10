"""
Define padrões de URL para blogs.
"""

from django.urls import path
from . import views

urlpatterns = [
    # Página incial.
    path('', view.index, name='index'),
]
