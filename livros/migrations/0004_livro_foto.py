# Generated by Django 4.2.4 on 2023-08-23 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0003_alter_livro_genero_delete_generos'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='livros/'),
        ),
    ]