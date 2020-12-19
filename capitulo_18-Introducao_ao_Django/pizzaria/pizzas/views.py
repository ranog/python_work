from django.shortcuts import render

# Create your views here.

def index(request):
    """A página inicial de Pizzaria."""     return render(request, 'pizzas/index.html')


def cardapio(request):
    """Lista todas as pizzas."""
    cardapio = Pizza.objects.order_by('date_added')
    context = {'cardapio': cardapio}
    return render(request, 'pizzas/cardapio.html', context)


