from django.shortcuts import render

# Create your views here.
def contactez_nous(request):
    return render(request, 'contactez_page/contactez_nous.html')


def  proposer_evnte(request):
    return render(request,'contactez_page/proposer_evnte.html')


def contactez_nous(request):
    return render(request,'contactez_page/contactez_nous.html')


def recrutement(request):
    return render(request,'contactez_page/recrutement.html')