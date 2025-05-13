from django.db import models

# Create your models here.
class Insertion_membre(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=150)
    email = models.CharField(max_length=250)
    mot_de_passe = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="static/image/membre")