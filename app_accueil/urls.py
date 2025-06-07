from django.urls import path
from.views import *

urlpatterns = [
    path("",affiche_index,name="accueil"),
    path("detail/<int:id>",affiche_detail,name="detail"),
    path("Tous_Produit",affiche_tous,name="Tous_Produit")
]