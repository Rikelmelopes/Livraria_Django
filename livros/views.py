
from livros.models import Livro
from livros.forms import LivroModelForm
from django.views.generic import ListView ,CreateView, DetailView, DeleteView
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
#class LivrosView(View):   
    
    #def get(self,request):
        #livros = Livro.objects.all().order_by('titulo')
        #search = request.GET.get('search')
    
        #if search:
            #livros = livros.filter(titulo__icontains=search)
        
        #return render(
        #request,
        #'livros.html',
        #{'livros':livros}
    #)

class LivroListView(ListView): #Template de uma lista
    model = Livro
    template_name = 'livros.html'
    context_object_name = 'livros'

    def get_queryset(self):
        livros = super().get_queryset().order_by('titulo')
        search = self.request.GET.get('search')
        if search:
            livros = livros.filter(titulo__icontains=search)
        return livros

    
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
#class NovoLivroView(View): #Class BasedViews
    
    #def get(self,request):
        #novo_livro_form = LivroModelForm()
        #return render(request,'novo_livro.html',{'novo_livro_form': novo_livro_form})
    
    #def post(self,request):
        #novo_livro_form = LivroModelForm(request.POST,request.FILES)
        #if novo_livro_form .is_valid():
            #novo_livro_form.save()
            #return redirect('livro_list') 
        #return render(request,'novo_livro.html',{'novo_livro_form': novo_livro_form})
        
class NewLivroListView(CreateView):
    model = Livro
    form_class = LivroModelForm
    template_name = 'novo_livro.html'
    success_url = '/livros/'
 
 
 