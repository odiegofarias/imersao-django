from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from tarefas.forms import TarefaNovaForm
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
            return render(request, 'tarefas/index.html', {'form': form, 'tarefas_pendentes': tarefas_pendentes}, status=400)
            
    tarefas_pendentes = Tarefa.objects.filter(feita=False).all()
    return render(request, 'tarefas/index.html', {'tarefas_pendentes': tarefas_pendentes})

