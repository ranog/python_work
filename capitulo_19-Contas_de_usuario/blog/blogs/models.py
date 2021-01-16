from django.db import models

# Create your models here.


class BlogPost(models.Model):
    """
        Um assunto sobre o qual o usuário está aprendendo.
    """
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    def __str(self):
        """
            Devolve uma representação em string do modelo.
        """
        return self.title
