"""
    Define padrões de URL para users.
"""

# No livro:
# from django.conf.urls import url
# from django.contrib.auth.views import login
from django.urls import path
#from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    # Página de login.
    path("login/", LoginView.as_view(template_name="users/login.html"),name="login"),

    # Página de logout.
    path("logout/", views.logout_view, name='logout')
]
