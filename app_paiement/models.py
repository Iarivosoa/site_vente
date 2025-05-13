from django.db import models
from app_membre.models import Insertion_membre
# Create your models here.
class paiement(models.Model):
    Produit = models.TextField()
    id_utilisateur = models.ForeignKey(Insertion_membre,on_delete=models.CASCADE)
    id_stripe = models.TextField()
    date_paiement = models.DateTimeField()