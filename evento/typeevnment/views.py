from django.shortcuts import render

# Create your views here.
def even_culturels(request):
    return render(request, 'typeevenment_page/even_culturels.html')


def  even_politiques(request):
    return render(request,'typeevenment_page/even_politiques.html')


def even_religieux(request):
    return render(request,'typeevenment_page/even_religieux.html')


def even_scientifiques(request):
    return render(request,'typeevenment_page/even_scientifiques.html')