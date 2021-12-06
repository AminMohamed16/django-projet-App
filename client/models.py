from django.db import models

# Create your models here.


class Client(models.Model):

    nom=models.CharField(max_length=200,null=True)

    telephon=models.CharField(max_length=200,null=True)

    dete_creation=models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
                return self.nom
