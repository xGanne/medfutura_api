from django.db import models

# Create your models here.
class Pessoa(models.Model):
    apelido = models.CharField(max_length=32, unique=True)
    nome = models.CharField(max_length=100)
    nascimento = models.DateField()
    stack = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.apelido