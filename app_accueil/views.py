from django.shortcuts import render
from .models import insertion_produit
from django.core.paginator import Paginator
from django.db import connection

# Create your views here.
def affiche_index(request):
    recup_produit = insertion_produit.objects.all()
    pagination = Paginator(recup_produit,6)
    page_num = request.GET.get('page',1)
#recuperation des types produits
    recup_type = set(article.type for article in recup_produit)
    
    
    try:
        page = pagination.page(page_num)
    except:
        page = pagination.page(1)
    contenu = {
        "produit":page,
        "TousProduit":recup_produit,
        "affiche_type":recup_type
    }

    return render(request,'index.html',contenu)

#AFFICHE DETAIL
def affiche_detail(request,id):
    recup_detail = insertion_produit.objects.get(pk=id)
    id_produit = id

    with connection.cursor() as curseur:
        curseur.execute("""
            SELECT app_commenteMembre_commentemembre.*,app_membre_insertion_membre.*
            FROM app_commenteMembre_commentemembre 
            INNER JOIN app_membre_insertion_membre 
            ON app_commenteMembre_commentemembre.id_membre = app_membre_insertion_membre.id 
            WHERE app_commenteMembre_commentemembre.id_pro = %s                   
        """, [id_produit])

        affiche_commente =curseur.fetchall()


    contenu = {
        "detail":recup_detail,
        "nombre_commentaire":len(affiche_commente),
        "commentaire": affiche_commente
    }

    return render(request,'detail.html',contenu)

# TOUS PRODUIT AFFICHAGE
def affiche_tous(request):
    recup_produit = insertion_produit.objects.all()
    valeur_rechercher = request.GET.get('recherche')
    resultat = []

    if valeur_rechercher:
        resultat = insertion_produit.objects.filter(
            nom__icontains = valeur_rechercher
        )
    contenu = {
        "TousProduit":recup_produit,
        "tous_valeur":valeur_rechercher,
        "resultats":resultat
    }
    return render(request,'tousProd.html',contenu)