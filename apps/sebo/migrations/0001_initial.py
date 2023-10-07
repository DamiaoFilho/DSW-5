# Generated by Django 4.2.6 on 2023-10-05 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.TextField(max_length=100, verbose_name='Descrição')),
                ('stamp', models.ImageField(upload_to='media/')),
                ('year', models.DateField()),
                ('country', models.TextField(max_length=100)),
                ('genre', models.TextField(max_length=100)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
