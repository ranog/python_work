from django.db import models

# Create your models here.

""" 18.4 – Pizzaria:

Inicie um novo projeto chamado pizzaria com uma aplicação chamada
pizzas.

Defina um modelo Pizza com um campo chamado name, que armazenará nomes
como Hawaiian e Meat Lovers.

Defina um modelo chamado Topping com campos de nome pizza e name.

O campo pizza deve ser uma chave estrangeira para Pizza, e name deve ser
capaz de armazenar valores como pineapple, Canadian bacon e sausage.

Registre os dois modelos no site de administração e use esse site para
fornecer alguns nomes de pizzas e de ingredientes.

Utilize o shell para explorar os dados inseridos. """

class Pizza(models.Model):
    """Nome de pizzas da pizzaria."""

    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.name


class Topping(models.Model):
    """Cobertura das pizzas."""

    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    class META:
        verbose_name_plural = 'toppings'


    def __str__(self):
        """Devolve uma representação em string do modelo."""

        if len(self.name) > 50:
            return self.name[:50] + "..."
        return self.name
