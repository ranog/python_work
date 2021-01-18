from django import forms
from . models import BlogPost


class BlogPostForm(forms.ModelForm):
    """
        Crie um formulário de um novo post.
    """
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': '', 'text': ''}
