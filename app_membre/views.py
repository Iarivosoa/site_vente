from django.shortcuts import render,redirect
from .models import Insertion_membre
import os
import hashlib
from django.contrib.auth import logout
from django.shortcuts import redirect
# Create your views here.
def connexion_page(request):
    return render(request,'connexion.html')
def souscription(request):
    return render(request,'souscription.html')

#CRYPTAGE MOT DE PASSE:
def cryptage_mdp(mdp):
    crypt_mdp = hashlib.sha1()
    crypt_mdp.update(mdp.encode("utf-8"))
    return crypt_mdp.hexdigest()

#INSERTION PHOTO MEMBRE 
def inserer_photo(request,photo):
    if"photo" in request.FILES:
        photo_membre = request.FILES['photo']
        chemin_photo = os.path.splitext(photo_membre.name)
        nouveau_nom = f"{photo}{chemin_photo[1]}"
        emplacement_photo = os.path.join("static/image/membre",nouveau_nom)

        with open(emplacement_photo,"wb") as destination_photo:
            for photo_utilisateur in photo_membre.chunks():
                destination_photo.write(photo_utilisateur)
                return nouveau_nom

# SOUSCRITPION MEBRE
def souscription_membre(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        mot_de_passe = request.POST.get('mot_de_passe')
        confirmer_mdp = request.POST.get('confirmer_mdp')

        if nom !="" and prenom !="" and email !="" and mot_de_passe !="" and confirmer_mdp != "":
            recup_email = Insertion_membre.objects.filter(email = email)
            nombre_email = len(recup_email)

            if nombre_email == 0:

                if mot_de_passe == confirmer_mdp:

                    Inserer = Insertion_membre(
                        nom = nom,
                        prenom = prenom,
                        email = email,
                        mot_de_passe = cryptage_mdp(mot_de_passe),
                        photo = f"static/image/membre/{inserer_photo(request,nom)}"
                    )
                    Inserer.save()
                    return render(request,"connexion.html")
                else:
                    erreur = "le mot de passe n'est pas identique"
                    return render(request,'souscription.html',{"erreurs":erreur})

            else:
                erreur = "cet email existe"
                return render(request,'souscription.html',{"erreurs":erreur})
                

        
        else:
            erreur ="Tous les champs sont obligatoire"
            return render(request,'souscription.html',{"erreurs":erreur})





    return render(request,'connexion.html')

# AUTHENTIFICATION MEMBRE
def connexion_membre(request):
    if request.method == "POST":
        email =  request.POST.get('email')
        mot_de_passe = request.POST.get('mot_de_passe')
        validation = True

        if email !="" and mot_de_passe !="":
            recup_email = Insertion_membre.objects.get(email = email)
            if cryptage_mdp(mot_de_passe) == recup_email.mot_de_passe:
                validation = True
                pass
            else:
                validation = False
                erreur = "Mot de passe incorrecte"
                return render(request,'connexion.html',{"erreurs":erreur})
        else:
            validation = False
            erreur = "Tous les champs sont obligatoires"
            return render(request,'connexion.html',{"erreurs":erreur})
        
        if validation:
            recup_user = {
                "id":recup_email.id,
                "nom_membre":recup_email.nom,
                "email_membre":recup_email.email,
                "photo_membre":str(recup_email.photo)
            }
            if validation:
                request.session["client"] = recup_user
                donner = recup_user
                return render(request,'bienvenu.html',{"donners":donner})
    return render(request,'connexion.html')

def custom_logout(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/connexion')