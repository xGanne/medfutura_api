from django.contrib import admin
from .models import Pessoa

# Register your models here.
@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['apelido', 'nome', 'nascimento', 'stack']