from django.db import models

# Create your models here.

"""---------------------------------------------------------------------

Criamos uma classe chamada Topic, que herda de Model – uma
classe-pai incluída em Django, que define a funcionalidade básica de um
modelo.

A classe Topic tem apenas dois atributos: text e date_added.

O atributo text é um CharField – um dado composto de caracteres, isto é,
um texto.

Usamos CharField quando queremos armazenar uma pequena quantidade de
texto, por exemplo, um nome, um título ou uma cidade.

Quando definimos um atributo CharField, devemos dizer a Django quanto
espaço deve ser reservado no banco de dados.

Nesse caso, especificamos um max_length de 200 caracteres, que deverá
ser suficiente para armazenar a maioria dos nomes de assuntos.

O atributo date_added é um DateTimeField – um dado que registrará uma
data e uma hora.

Passamos o argumento auto_now_add=True, que diz a Django para definir
esse atributo automaticamente com a data e hora atuais sempre que o
usuário criar um novo assunto.

NOTA

Para ver os diferentes tipos de campos que você pode usar em um modelo,
consulte o Django Model Field Reference (Referência aos campos do modelo
de Django) em https://docs.djangoproject.com/en/1.8/ref/models/fields/.

Devemos dizer a Django qual atributo deve ser usado como default quando
ele exibir informações sobre um assunto.

O Django chama um método __str__() para exibir uma representação simples
de um modelo.

Nesse caso, escrevemos um método __str__() que devolve a string
armazenada no atributo text."""


class Topic(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo."""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.text


""" Definindo o modelo Entry (pg 455-456):

    A classe Entry herda da classe base Model de Django, assim como foi
    feito com Topic.

    O primeiro atributo, topic, é uma instância de ForeignKey.

    Uma chave estrangeira (foreign key) é um termo usado em banco de
    dados: é uma referência a outro registro do banco de dados.

    Esse é o código que associa cada entrada a um assunto específico.

    Cada assunto recebe uma chave, isto é, um ID, quando é criado.

    Quando Django precisa estabelecer uma conexão entre dois dados, ele
    usa a chave associada a cada informação.

    Em seguida, temos um atributo chamado text, que é uma instância de
    TextField.

    Esse tipo de campo não precisa de um limite para o tamanho, pois não
    queremos restringir o tamanho das entradas individuais.

    O atributo date_added nos permite apresentar as entradas na ordem em
    que foram criadas e inserir um timestamp junto a cada entrada.

    Aninhamos a classe Meta em nossa classe Entry.

    Meta armazena informações extras para administrar um modelo; nesse
    caso, ela nos permite definir um atributo especial que diz a Django
    para usar Entries quando precisar se referir a mais de uma entrada.
    (Sem isso, Django iria referenciar várias entradas como Entrys.)

    Por fim, o método __str__() diz a Django quais informações devem ser
    mostradas quando entradas individuais forem referenciadas.

    Como uma entrada pode ser um texto longo, dizemos a Django para
    mostrar apenas os primeiros 50 caracteres de text.

    Também acrescentamos reticências para deixar claro que não estamos
    exibindo a entrada completa."""


class Entry(models.Model):
    """Algo específico aprendido sobre um assunto."""

    # Um relacionamento muitos para um.  Requer dois argumentos
    # posicionais: a classe à qual o modelo está relacionado e a opção
    # on_delete. 
    # Site acessado em 13 de dezembro de 2020:
    # https://docs.djangoproject.com/pt-br/3.1/ref/models/fields/#django.db.models.ForeignKey
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    class META:
        verbose_name_plural = 'entries'


    def __str__(self):
        """Devolve uma representação em string do modelo."""


        """ 18.2 – Entradas menores (pg 459-460):
            No momento, o método __str__() no modelo Entry concatena
            reticências a todas as instâncias de Entry quando Django
            exibe uma entrada no site de administração ou no shell.
            Acrescente uma instrução if no método __str__() que adicione
            reticências somente se a entrada tiver mais de 50
            caracteres. Utilize o site de administração para acrescentar
            uma entrada com menos de 50 caracteres e certifique-se de
            que ela não contenha reticências quando for visualizada."""

        if len(self.text) > 50:
            return self.text[:50] + "..."
        return self.text
