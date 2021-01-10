from django.shortcuts import render

# Create your views here.

from . models import BlogPost

def index(request):
    """ 
    Página inicial que mostra todas as postagens.
    """
    blog_post = BlogPost.objects.order_by('date_added')
    context = {'blog_post': blog_post}
    return render(request, 'blogs/index.html', context)
