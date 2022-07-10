from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from tarefas.forms import TarefaNovaForm, TarefaForm
from django.urls import reverse
from tarefas.models import Tarefa



# Create your views here.
def index(request):
    # Verificando o metodo
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        # Verificando se é valido e salvando
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tarefas:index'))
        else:
            tarefas_pendentes = Tarefa.objects.filter(feita=False).all()
            tarefas_feitas = Tarefa.objects.filter(feita=True).all()
            return render(
                request, 'tarefas/index.html', 
                {
                    'form': form, 
                    'tarefas_pendentes': tarefas_pendentes,
                    'tarefas_feitas': tarefas_feitas,
                }, 
                status=400
            )

    tarefas_pendentes = Tarefa.objects.filter(feita=False).all()
    tarefas_feitas = Tarefa.objects.filter(feita=True).all()
    return render(
        request, 'tarefas/index.html', 
        {
            'tarefas_pendentes': tarefas_pendentes,
            'tarefas_feitas': tarefas_feitas,
        }
    )


def detalhe(request, tarefa_id):
    if request.method == 'POST':
        tarefa = Tarefa.objects.get(id=tarefa_id)
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()

    return HttpResponseRedirect(reverse('tarefas:index'))


def apagar(request, tarefa_id):
    if request.method == 'POST':
        Tarefa.objects.filter(id=tarefa_id).delete()
    return HttpResponseRedirect(reverse('tarefas:index'))
