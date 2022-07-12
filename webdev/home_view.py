from django.http import HttpResponseRedirect
from django.urls import reverse

# redirecionando para tarefas
def home(request):
    return HttpResponseRedirect(reverse('tarefas:index'))
