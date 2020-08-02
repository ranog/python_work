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


""" Algo específico aprendido sobre um assunto. """

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta: verbose_name_plural = 'entries'

    """ Devolve uma representação em string do modelo. """
    def __str__(self):

        if len(self.text) > 50:
            return self.text[:50] + "..."

        return self.text

""" A classe Entry herda da classe base Model de Django, assim como foi feito
com Topic. O primeiro atributo, topic, é uma instância de ForeignKey. Uma chave
estrangeira (foreign key) é um termo usado em banco de dados: é uma referência
a outro registro do banco de dados. Esse é o código que associa cada entrada a
um assundo específico. Cada assunto recede um chave, isto é, um ID, quando é
criado.

O atributo text é uma instância de TextField. Esse tipo de campo não precisa de
um limite para o tamanho, pois não queremos restringir o tamanho das entradas
individuais.

O atributo date_added nos permite apresentar as entradas na ordem em que foram
criadas e inserir um timestamp junto a cada entrada.

Aninhamos a classe Meta em nossa classe Entry. Meta armazena informações extras
para administrar um modelo; nesse caso, ela nos permite definir um atributo
especial que diz a Django para usar Entries quando precisar se referir a mais
de uma entrada (Sem isso, Django iria referenciar várias entradas como
Entrys).

O método __str__() diz a Django quais informações devem ser mostradas quando
entradas individuais forem referenciadas. Como uma entrada pode ser um texto
longo, dizemos a Django para mostrar apenas os primeiros 50 caracteres de text.
Também acrescentamos reticências para deixar claro que não estamos exibindo a
entrada completa. """
