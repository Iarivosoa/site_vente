from django.db import models

# Create your models here.
class insertion_produit(models.Model):
    nom = models.CharField(max_length=250)
    description = models.TextField()
    prix = models.FloatField()
    photo = models.ImageField(upload_to="static/image")
    photo2 = models.ImageField(upload_to="static/image")
    photo3 = models.ImageField(upload_to="static/image")
    type = models.CharField(max_length=250)

def __str__(self):
    return self.nom
