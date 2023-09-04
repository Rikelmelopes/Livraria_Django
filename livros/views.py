from django.shortcuts import render,redirect
from livros.models import Livro
from livros.forms import LivroModelForm
from django.views import View
# Create your views here.

#Function BasedViews
'''def livros_view(request):

    livros = Livro.objects.all().order_by('titulo')
    search = request.GET.get('search')
    
    if search:
        livros = livros.filter(titulo__icontains=search)
        
    return render(
        request,
        'livros.html',
        {'livros':livros}
    )'''
class LivrosView(View):   #Class BasedViews
    
    def get(self,request):
        livros = Livro.objects.all().order_by('titulo')
        search = request.GET.get('search')
    
        if search:
            livros = livros.filter(titulo__icontains=search)
        
        return render(
        request,
        'livros.html',
        {'livros':livros}
    )

#Function BasedViews
'''def novo_livro_view(request):
    if request.method == 'POST':
        novo_livro_form = LivroModelForm(request.POST,request.FILES)
        if novo_livro_form.is_valid():
            novo_livro_form.save()
            return redirect('livro_list')
    else:
        novo_livro_form = LivroModelForm()
    return render (request, 'novo_livro.html',{'novo_livro_form':novo_livro_form})'''
class NovoLivroView(View): #Class BasedViews
    
    def get(self,request):
        novo_livro_form = LivroModelForm()
        return render(request,'novo_livro.html',{'novo_livro_form': novo_livro_form})
    
    def post(self,request):
        novo_livro_form = LivroModelForm(request.POST,request.FILES)
        if novo_livro_form .is_valid():
            novo_livro_form.save()
            return redirect('livro_list') 
        return render(request,'novo_livro.html',{'novo_livro_form': novo_livro_form})