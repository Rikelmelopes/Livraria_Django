
from livros.models import Livro
from livros.forms import LivroModelForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView ,CreateView, DetailView , UpdateView , DeleteView
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
@method_decorator(login_required(login_url='login'), name='dispatch')   
class NewLivroListView(CreateView):
    model = Livro
    form_class = LivroModelForm
    template_name = 'novo_livro.html'
    success_url = '/livros/'
 
  
class LivroDetailView(DetailView):
    model = Livro
    template_name = 'livro_detail.html'

@method_decorator(login_required(login_url='login'), name='dispatch')   
class LivroUpdateView(UpdateView):
    model = Livro
    form_class = LivroModelForm
    template_name = 'livro_update.html'
 
    def get_success_url(self):
        return reverse_lazy('detalhes_livros', kwargs={'pk': self.object.pk})
    
@method_decorator(login_required(login_url='login'), name='dispatch')     
class LivroDeleteView(DeleteView):
    model = Livro
    template_name = 'livro_delete.html'
    success_url = '/livros/'