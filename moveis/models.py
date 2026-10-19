from django.db import models

class Movel(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    material = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# Create your models here.
