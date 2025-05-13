from django.urls import path
from.views import*

urlpatterns = [
    path("connexion",connexion_page,name="connexion"),
    path("souscription",souscription,name="souscription"),
    #PATH SOUSCRIPTION
    path("souscription_membre",souscription_membre,name="souscription_membre"),
    #path connexion membre
    path("connexion_membre/",connexion_membre,name="connexion_membre"),
    #deconnexion
    path('logout',custom_logout,name='logout'),
]