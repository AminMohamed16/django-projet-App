from django.shortcuts import render
from .models import Client
# Create your views here.


def list_client(request,pk):
    client=Client.objects.get(id=pk)
    Commande=client.commande_set.all()
    commande_total=Commande.count()
    context={'Client':client,'Commande':Commande,'commande_total':commande_total}

    return render(request, 'client/list_client.html',context)
