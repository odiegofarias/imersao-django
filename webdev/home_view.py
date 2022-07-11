from django.http import HttpResponseRedirect

# redirecionando para tarefass
def home(request):
    return HttpResponseRedirect(reverse('tarefas:index'))
