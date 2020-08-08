from django.db import models

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=200)

    """ para registrar date e hora sempre quando for criar uma nova pizza. """
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta: verbose_name_plural = 'topping'

    def __str__(self):
        if len(self.name) > 50:
            return self.name[:50] + " ..."

        return self.name
