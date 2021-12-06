from django.urls import path
from . import views

urlpatterns = [
    path('',views.evenment_actuels),
    path('evenment_precedent/',views.evenment_precedent),
    path('evenment_venir/',views.evenment_venir),
    
]