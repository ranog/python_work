""" Inicialmente importamos o módulo forms e o modelo Topic com o qual
trabalharemos.
    
    Definimos uma classe chamada TopicForm que herda de forms.ModelForm.

    A versão mais simples de um ModelForm é constituída de uma classe
    Meta aninhada que diz a Django em qual modelo o formulário deve se
    basear e quais campos devem ser incluídos nesse formulário.

    Criamos um formulário a partir do modelo Topic e incluímos apenas o
    campo text.

    O código labels = {'text': ''} diz a Django para não gerar um rótulo
    para o campo text.

------------------------------------------------------------------------

    Inicialmente atualizamos a instrução import para incluir Entry, além
    de Topic.

    A nova classe EntryForm herda de forms.ModelForm e tem uma classe
    Meta aninhada que lista o modelo no qual ela está baseada e o campo
    a ser incluído no formulário.

    Novamente especificamos um rótulo vazio para o campo 'text'.

    Incluímos o atributo widgets.

    Um widget é um elemento de formulário HTML, por exemplo, uma caixa
    de texto de uma única linha, uma área de texto com várias linhas ou
    uma lista suspensa.

    Ao incluir o atributo widgets, podemos sobrescrever as opções
    default de widgets de Django.

    Ao dizer a Django para usar um elemento forms.Textarea, estamos
    personalizando o widget de entrada para o campo 'text' de modo que a
    área de texto tenha 80 colunas, em vez de usar o default de 40.

    Isso dará espaço suficiente aos usuários para redigir uma entrada
    significativa."""

from django import forms

from . models import Topic, Entry


class TopicForm(forms.ModelForm):
    """Cria um formulário."""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    """Criar um formulário associado ao modelo Entry."""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
