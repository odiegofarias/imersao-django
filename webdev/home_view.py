from django.http import HttpResponse


def home(request):
    return HttpResponse(request, HttpResponse('Bem vindo Django PRO'))
