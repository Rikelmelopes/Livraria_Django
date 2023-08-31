from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm


def registro_view(request):
    if request.methpd == 'POST':
        usuario_form = UserCreationForm(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()
            return redirect('login')
    else:
        usuario_form = UserCreationForm()
    return render(request, 'registro.html',{'usuario_form':usuario_form})