from django.db import models

# Create your models here.


class Disk(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    description = models.TextField(max_length=100, verbose_name="Descrição")
    stamp = models.CharField(max_length=100, verbose_name="Selo")
    year = models.DateField(verbose_name="Ano")
    country = models.TextField(max_length=100, verbose_name="País")
    genre = models.TextField(max_length=100, verbose_name="Gênero")
    quantity = models.IntegerField(verbose_name="Quantidade")