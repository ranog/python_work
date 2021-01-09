"""
------------------------------------------------------------------------

DESCRIÇÃO
        FAÇA VOCÊ MESMO

        19.1 – Blog: Inicie um novo projeto Django chamado Blog.

        Crie uma aplicação chamada blogs no projeto, com um modelo de
        nome BlogPost.

        O modelo deve ter campos como title, text e date_added.

        Crie um superusuário para o projeto e use o site de
        administração para inserir algumas postagens pequenas.

        Crie uma página inicial que mostre todos as postagens em ordem
        cronológica.

        Construa um formulário para criar novas postagens e outro para
        editar postagens existentes.

        Preencha seus formulários para garantir que funcionem.

        Esse código importa o modelo que queremos registrar, BlogPost, e
        então usa admin.site.register() v para dizer a Django que
        administre nosso modelo por meio do site de administração.

------------------------------------------------------------------------

HISTÓRICO
        20210901: João Paulo, janeiro de 2021.
            - 19.1 – Blog (pg 489).

------------------------------------------------------------------------
"""

from django.contrib import admin

# Register your models here.

from blogs.models import BlogPost
admin.site.register(BlogPost)
