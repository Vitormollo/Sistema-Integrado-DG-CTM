from django.db import models

# Create your models here.
class Conselheiro(models.Model):
    id_conselheiro = models.AutoField(primary_key=True)
    nm_conselheiro = models.CharField(max_length=255)
    

    def __str__(self):
        return self.nm_conselheiro