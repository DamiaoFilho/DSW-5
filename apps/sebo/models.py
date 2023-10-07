from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    description = models.TextField(max_length=100, verbose_name="Descrição")
    stamp = models.CharField(max_length=100, verbose_name="Selo")
    year = models.DateField(verbose_name="Ano")
    country = models.TextField(max_length=100, verbose_name="Ano")
    genre = models.TextField(max_length=100, verbose_name="Ano")
    quantity = models.IntegerField(verbose_name="Ano")