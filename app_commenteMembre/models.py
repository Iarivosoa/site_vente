from django.db import models
from app_membre.models import Insertion_membre
from app_accueil.models import insertion_produit
# Create your models here.
class CommenteMembre(models.Model):
    id_pro = models.IntegerField(models.ForeignKey(insertion_produit,on_delete=models.CASCADE))
    id_membre = models.IntegerField(models.ForeignKey(Insertion_membre,on_delete=models.CASCADE))
    commentaire = models.TextField()
    date = models.DateTimeField()