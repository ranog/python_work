from django.shortcuts import render

# Create your views here.

from . models import BlogPost


def index(request):
    """A página inicial de Blog."""
    return render(request, 'blogs/index.html')
