from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskList, name='task-list'),
    path('cadastro', views.cadastroClientes, name='cadastro'),
    path('update/<int:id>', views.update, name='update')
]