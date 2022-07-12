from django.http import HttpResponse


def index(request):
    return HttpResponse(request, 'Olá, Django PRO')