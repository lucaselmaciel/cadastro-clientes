from django.core import paginator
from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator
from .forms import CadastroModelForm
from .models import CadastroCliente
from django.contrib import messages


# Create your views here.

def cliList(request):
    cliente = CadastroCliente.objects.all().order_by('-criacao')

    pag = Paginator(cliente, 5)
    
    page = request.GET.get('page')

    clientes = pag.get_page(page)

    context = {
        'tasks': clientes
    }    
    return render(request, 'tasks/list.html', context)

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

def conteudo(request, id):
    cliente = get_object_or_404(CadastroCliente, pk=id)
    status = 'Ativo' if cliente.ativo else 'Inativo'
    context = {
        'cliente': cliente,
        'status': status
    }
    return render(request, 'tasks/conteudo.html', context)

def update(request, id):
    cliente = CadastroCliente.objects.get(id=id)
    form = CadastroModelForm(instance=cliente)
    

    context = {
        'cliente': cliente,
        'form': form,
    }
    if str(request.method)=='POST':
        form = CadastroModelForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'tasks/update.html', context)
    else:
        return render(request, 'tasks/update.html', context)

def delete(request, id):
    cliente = get_object_or_404(CadastroCliente, pk=id)
    cliente.delete()
    return render(request, 'tasks/delete.html')