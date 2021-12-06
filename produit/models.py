from django.db import models

# Create your models here.


class Tag(models.Model):
    nom=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom=models.CharField(max_length=200,null=True)
    prix=models.FloatField(null=True)
    dete_creation=models.DateTimeField(auto_now_add=True,null=True)
    tag=models.ManyToManyField(Tag)

    def __str__(self):
        return self.nom
