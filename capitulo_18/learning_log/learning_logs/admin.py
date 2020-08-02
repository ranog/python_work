from django.contrib import admin

# Register your models here.

from learning_logs.models import Topic, Entry
admin.site.register(Topic)
admin.site.register(Entry)

""" Esse código importa o modelo que queremos registrar, Topic, e então usa
admin.site.register() para dizer a Django que administre nosso modelo por meio
do site de administração. """
