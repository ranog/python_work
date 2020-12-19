from django.shortcuts import render

# Create your views here.
from . models import Pizza


def index(request):
    """A página inicial de Pizzaria."""     
    return render(request, 'pizzas/index.html')


def pizzas(request):
    """Lista todas as pizzas."""
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/cardapio.html', context)


def ingredientes(request, pizza_id):           
    """Mostra um único assunto e todas as suas entradas."""                     
    ingredientes = Pizza.objects.get(id=pizza_id)                                      
    entries = ingredientes.entry_set.order_by('-date_added')                           
    context = {'ingredientes': ingredientes, 'entries': entries}                              
    return render(request, 'pizzas/ingredientes.html', context)
