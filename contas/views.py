from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login , logout


def registro_view(request):
    if request.method == 'POST':
        usuario_form = UserCreationForm(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()
            return redirect('login')
    else:
        usuario_form = UserCreationForm()
    return render(request, 'registro.html',{'usuario_form':usuario_form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password= password)
        if user is not None:
            login(request,user)
            return redirect('livro_list')
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
    return render(request,'login.html',{'login_form':login_form})

def logout_view(request):
    logout(request)
    return redirect('livro_list')