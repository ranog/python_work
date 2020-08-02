from django.db import models

# Create your models here.

""" Um assunto sobre o qual o usuário está aprendendo. """
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Devolve uma representação em string do modelo. """
        return self.text

""" Criamos uma clase chamada Topic, que herda de Model uma classe-pai incluída
em Django, que define a funcionalidade básica de um modelo. A classe Topic tem
apenas dois atributos: text e date_added.

O atributo text é um CharField - um dado composto de caracteres, isto é, um
texto. Usamos CharField quando queremos armazenar uma pequena quantidade de
texto, por exemplo, um nome, um título ou uma cidade. Quando definimos um
atributo CharField, devemos dizer a o Django quanto espaço deve ser reservado
no banco de dados. Nesse caso, especificamos um max_length de 200 caracteres,
que deverá ser suficiente para armazenar a maioria dos nomes de assuntos.

O atributo date_added é um DateTimeField - um dado que registrará uma data e
uma hora. Passamos o argumento auto_now_add=True, que diz a Django para definir
esse atributo automaticamente com a data e hora atuais sempre que o usuário
criar um novo assunto.

Devemos dizer a Django qual atributo deve ser usado como default quando ele
exibir informações sobre um assunto. O Django chama um método __str__() para
exibir uma representação simples de um modelo. Nesse caso, escrevemos um método
__str__() que devolve a string armazenada no atributo text. """
