from django.http import HttpResponse


def index(request):
    return HttpResponse('Olá, Django PRO')