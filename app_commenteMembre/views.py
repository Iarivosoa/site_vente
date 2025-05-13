from django.shortcuts import render,redirect
from django.utils import timezone
from .models import CommenteMembre
# Create your views here.
def commentaire(request):
    if request.method == "POST":
        commentaire = request.POST.get("commentaire")
        id_produit = request.POST.get("id_produit")
        id_membre = request.session["client"]["id"]
        date = timezone.now().strftime("%Y-%m-%d")


        if commentaire !="":
            Inserer_commente = CommenteMembre(
                id_pro = id_produit,
                id_membre = id_membre,
                commentaire = commentaire,
                date = date

            )
            Inserer_commente.save()
            return redirect(f"http://127.0.0.1:8000/detail/{id_produit}",{"message":"Commentaire envoyer"})
        else:
            return redirect(f"http://127.0.0.1:8000/detail/{id_produit}",{"message":"champs obligatoire"})



        
    return redirect(f"http://127.0.0.1:8000/detail/{id_produit}",{"id":commentaire})

def suppression_commente(request,id_commente):

    recup_commente = CommenteMembre.objects.get(id = id_commente)
    id_produit = request.POST.get("id_produit")
    if recup_commente:
        recup_commente.delete()
    return redirect(f"http://127.0.0.1:8000/detail/{id_produit}",{"id":commentaire})
