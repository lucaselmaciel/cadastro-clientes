from django import forms
from .models import CadastroCliente

class CadastroModelForm(forms.ModelForm):
    class Meta:
        model = CadastroCliente
        fields = ['ativo', 'nome', 'sobrenome', 'cpf', 'email', 'cep', 'logradouro', 'numero', 'bairro', 'cidade', 'uf', 'telefone']