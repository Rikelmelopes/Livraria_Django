# Generated by Django 4.2.4 on 2023-08-23 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_generos_alter_livro_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='genero',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Generos',
        ),
    ]
