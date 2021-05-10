from django.shortcuts import render
from .forms import CadastroModelForm
from .models import CadastroCliente
from django.contrib import messages


# Create your views here.

def taskList(request):
    return render(request, 'tasks/list.html')

def cadastroClientes(request):
    if str(request.method) == 'POST':
        form = CadastroModelForm(request.POST or None)
        if form.is_valid():
            form.save()

            form = CadastroModelForm()
            messages.success(request, 'Formulário enviado com sucesso')
        else:
            messages.error(request, 'Erro ao enviar formulário')
    else:
        form = CadastroModelForm()

    context = {
        'form': form
    }
    return render(request, 'tasks/cadastro.html', context)

'''def update(request, id):
    cliente = CadastroCliente.objects.get(id=id)
    context = {
        'cliente': cliente
    }
    return render(request, 'tasks/update.html', context)'''