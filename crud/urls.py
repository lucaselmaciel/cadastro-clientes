from django.urls import path
from . import views

urlpatterns = [
    path('', views.cliList, name='cliente-list'),
    path('cadastro', views.cadastroClientes, name='cadastro'),
    path('update/<int:id>', views.update, name='update'),
    path('conteudo/<int:id>', views.conteudo, name='conteudo'),
    path('delete/<int:id>', views.delete, name='delete')
]