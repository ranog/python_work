from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse

from . models import BlogPost
from . forms import BlogPostForm

def index(request):
    """
    Página inicial que mostra todas as postagens.
    """
    blog_post = BlogPost.objects.all().order_by('-date_added')
    context = {'blog_post': blog_post}
    return render(request, 'blogs/index.html', context)


def new_post(request):
    """
    Adiciona um novo post.
    """
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco.
        form = BlogPostForm()
    else:
        # Dados de POST submetidos; processa os dados.
        form = BlogPostForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)
