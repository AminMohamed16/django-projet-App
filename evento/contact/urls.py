from django.urls import path
from . import views

urlpatterns = [
    path('',views.contactez_nous,name='contactez'),
    path('proposer_evnte/',views.proposer_evnte),
    path('recrutement/',views.recrutement),
    
]