
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from livros.views import LivroListView ,NewLivroListView
from contas.views import registro_view, login_view , logout_view

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('logout/',logout_view,name='logout'),
    path('login/',login_view, name='login'),
    path('registro/',registro_view,name='registro'), 
    path('livros/',LivroListView.as_view(),name='livro_list'), 
    path('novo_livro/',NewLivroListView.as_view(),name= 'novo_livro')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
