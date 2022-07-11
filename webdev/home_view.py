from django.http import HttpResponseRedirect

# redirecionando para tarefas
def home(request):
    return HttpResponseRedirect(reverse('tarefas:index'))
