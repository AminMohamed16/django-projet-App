from django.http import request
from django.shortcuts import redirect, render
from .forms import CommandeForm
from .models import Commande

# Create your views here.

def list_commande(request):
    return render(request, 'commande/list_commande.html')

def ajouter_commande(request):
    form=CommandeForm()
    if request.method=='POST':
        form=CommandeForm(request.POST )
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'commande/ajouter_commande.html',context)


def modifier_commande(request,pk):
    commande=Commande.objects.get(id=pk)
    form=CommandeForm(instance=commande)
    if request.method=='POST':
        form=CommandeForm(request.POST ,instance=commande)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'commande/modifier_commande.html',context)


def supprimer_commande(request,pk):
    commande=Commande.objects.get(id=pk)
    if request.method=='POST':
            commande.delete()
            return redirect('/')
    context={'item':Commande}
    return render(request, 'commande/supprimer_commande.html',context)




