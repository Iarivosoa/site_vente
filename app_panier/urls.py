from django.urls import path
from.views import*



urlpatterns = [
    path("panier",page_panier,name="panier"),
    path("panier/<int:id>",ajouter_panier,name="ajouter_panier"),
    path("supprimer_prod/<int:id>",supprimer_prod,name="supprimer_prod"),

    #url paiement
    path("procedure_paiement",procedure_paiement,name="procedure_paiement"),

    #effectuer paie
    path('effectuer_paiement',effectuer_paiement,name='effectuer_paiement'),
    path("affiche_facture",affiche_facture,name="affiche_facture"),
    path("telecharge",telecharge,name="telecharge")
]