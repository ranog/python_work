from django.shortcuts import render

# Create your views here.

def index(request):
    """A página inicial de Pizzaria."""
    
    return render(request, 'pizzas/index.html')
