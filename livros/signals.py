from django.db.models.signals import post_save , post_delete
from django.dispatch import receiver
from django.db.models import Sum
from livros.models import Livro ,LivroInventory

def livro_inventory_update():
    quantidade_livros = Livro.objects.all().count()
    valor_livros = Livro.objects.aggregate(
        valor_total=Sum('valor')
    )['valor_total']

    LivroInventory.objects.create(
        quantidade_livros=quantidade_livros,
        valor_livros =valor_livros
    )

@receiver(post_save,sender=Livro)
def livro_post_save(sender, instance,  **kwargs):
    livro_inventory_update()

@receiver(post_delete,sender=Livro)
def livro_post_delete(sender, instance,  **kwargs):
    livro_inventory_update()