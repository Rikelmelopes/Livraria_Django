from django.db import models

# Create your models here.

class Livro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    data_lancamento = models.IntegerField(blank=True,null=True)
    valor = models.FloatField(blank=True,null=True)
    foto = models.ImageField(upload_to='livros/',blank=True,null=True)
    
    def __str__(self):
        return self.titulo