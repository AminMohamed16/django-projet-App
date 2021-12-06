from django.shortcuts import render

# Create your views here.
def evenment_actuels(request):
    return render(request, 'lesevnment_page/evenment_actuels.html')


def  evenment_venir(request):
    return render(request,'lesevnment_page/evenment_venir.html')


def evenment_precedent(request):
    return render(request,'lesevnment_page/evenment_precedent.html')

