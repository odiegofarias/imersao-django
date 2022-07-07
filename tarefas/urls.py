from django.urls import path
from . import views


app_name = 'tarefas'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:tarefa_id>', views.detalhe, name="detalhe"),
]
