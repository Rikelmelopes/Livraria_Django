
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from livros.views import livros_view ,novo_livro_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livros/',livros_view,name='livro_list'),
    path('novo_livro/',novo_livro_view,name= 'novo_livro')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
