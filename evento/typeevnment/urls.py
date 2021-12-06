from django.urls import path
from . import views

urlpatterns = [
    path('',views.even_culturels),
    path('even_politiques/',views.even_politiques),
    path('even_religieux/',views.even_religieux),
    path('even_scientifiques/',views.even_scientifiques),
]