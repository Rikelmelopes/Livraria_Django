from django import forms
from livros.models import Livro

class LivroModelForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'