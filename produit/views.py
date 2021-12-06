from django.http.response import HttpResponse
from django.shortcuts import render

from commande.models import Commande
from client.models import Client
# Create your views here.


def home(request):

    Commandes=Commande.objects.all()
    clients=Client.objects.all()
    context={'Commandes':Commandes,'clients':clients}

    return render(request, 'produit/acceuil.html',context)
