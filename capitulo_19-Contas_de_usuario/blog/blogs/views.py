from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from . models import BlogPost
from . forms import BlogPostForm


def index(request):
    """
        A página inicial que mostre todos as postagens em ordem
        cronológica.
    """
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)


@login_required
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
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('index'))

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


@login_required
def edit_post(request, post_id):
    """
        Edita um post existente.
    """
    review = BlogPost.objects.get(id=post_id)
    posts = review.text

    if review.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Requisição inicial; preenche previamente o formulário com a
        # entrada atual.
        form = BlogPostForm(instance=review)
    else:
        # Dados de POST submetidos; processa os dados.
        form = BlogPostForm(instance=review, data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))

    context = {'review': review, 'posts': posts, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
