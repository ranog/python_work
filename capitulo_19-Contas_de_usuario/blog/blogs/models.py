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

------------------------------------------------------------------------

HISTÓRICO
        20210701: João Paulo, janeiro de 2021.
            - 19.1 – Blog (pg 489).

------------------------------------------------------------------------
"""

from django.db import models

# Create your models here.

class BlogPost(models.Model):
    """
        Um assunto que foi postado no blog.
    """
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_add = models.DataTimeField(auto_now_add=True)


    def __str__(self):
        """
            Devolve uma representação em string do modelo.
        """
        return self.title
