from django import forms
from . models import BlogPost


class BlogPostForm(forms.ModelForm):
    """
    Cria automaticamente um formulário.
    """
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': '', 'text': ''}
