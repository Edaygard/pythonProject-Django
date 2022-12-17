import datetime
from.models import Transacao
from django.shortcuts import render


# Create your views here.
def home(request):
    data = {}
    data['now'] = datetime.datetime.now()
    return render(request, 'contas/home.html', data)


def listagem(request):
    data= {}
    data['transacoes'] = Transacao.objects.all()

    return render(request, 'contas/listagem.html', data)
