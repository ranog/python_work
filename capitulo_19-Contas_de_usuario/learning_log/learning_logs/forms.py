""" Inicialmente importamos o módulo forms e o modelo Topic com o qual
trabalharemos.
    
    Definimos uma classe chamada TopicForm que herda de forms.ModelForm.

    A versão mais simples de um ModelForm é constituída de uma classe
    Meta aninhada que diz a Django em qual modelo o formulário deve se
    basear e quais campos devem ser incluídos nesse formulário.

    Criamos um formulário a partir do modelo Topic e incluímos apenas o
    campo text.

    O código labels = {'text': ''} diz a Django para não gerar um rótulo
    para o campo text. """

from django import forms

from . models import Topic


class TopicForm(forms.ModelForm):
    """Cria um formulário."""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


