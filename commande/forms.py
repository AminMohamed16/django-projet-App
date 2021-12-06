from django.db import models
from django.forms import ModelForm, fields
from .models import Commande

class CommandeForm(ModelForm):
    class Meta:
        model=Commande
        fields='__all__'