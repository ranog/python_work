from django.shortcuts import render

# Create your views here.

from . models import BlogPost


def index(request):
    """
        A página inicial que mostre todos as postagens em ordem
        cronológica.
    """
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}

    return render(request, 'blogs/index.html', context)
