
from django.db import models
from django.contrib.auth.models import User

class Conselheira(models.Model):
    id_conselheira = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_conselheira = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_conselheira

class Secretaria(models.Model):
    id_secretaria = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_secretaria = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_secretaria