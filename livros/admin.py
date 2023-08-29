from django.contrib import admin
from livros.models import Livro
# Register your models here

class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo','genero','autor','data_lancamento','valor')
    search_fields = ('titulo','genero')
    
admin.site.register(Livro,LivroAdmin)