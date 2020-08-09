from django.shortcuts import render

# Create your views here.

""" A página inicial de Learning Log """

def index(request):
    return render(request, 'learning_logs/index.html')
