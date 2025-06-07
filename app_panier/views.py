from django.shortcuts import render,redirect
import stripe.error
import os
from app_accueil.models import insertion_produit
from app_membre.models import Insertion_membre
import stripe
from app_paiement.models import paiement
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
# from weasyprint import HTML
from django.http import HttpResponse
from django.template.loader import render_to_string
import io
from django.http import FileResponse
from .views import*



# Create your views here.
def page_panier(request):
    return render(request,'panier.html')
#AJOUTER UN ARTICLE DANS LE PANIER
def ajouter_panier(request,id):
    recup_article = insertion_produit.objects.get(pk = id)
    if "cart" not in request.session:
        request.session["cart"] = []
    
    stock_article = {
        "id_article":recup_article.id,
        "nom_article":recup_article.nom,
        "prix_article":recup_article.prix,
        "photo_article":str(recup_article.photo)
    }
    if stock_article not in request.session["cart"]:
        request.session["cart"].append(stock_article)
        request.session.modified = True
        return redirect('http://127.0.0.1:8000/panier')
    return redirect('http://127.0.0.1:8000/panier')

#SUPPRIMER UN ARTICLE DANS LE PANIER
def supprimer_prod(request,id):
    if "cart" in request.session:
        produit_panier = request.session["cart"]

        for index,valeur in enumerate(produit_panier):
            if valeur['id_article'] == id:
                del produit_panier[index]
                break
        request.session["cart"] = produit_panier
    return redirect('http://127.0.0.1:8000/panier')

    #PAIEMENT
def procedure_paiement(request):
    return render(request,'procedure_paiement.html')


# requette paiement
stripe.api_key = os.getenv("STRIPE_PRIVATE_KEY")

def effectuer_paiement(request):
    if request.method == "POST":
        token_stripe = request.POST.get('token_stripe')
        prix_finale = request.POST.get('prix_finale')
        commande = request.POST.get('commande')
        email_client = request.POST.get('email_client')

        recup_id = Insertion_membre.objects.get(id = int(request.session['client']['id']))

        try:
            creer_charge = stripe.Charge.create(
                amount = int(float(prix_finale)*100),
                currency="Eur",
                description=f"paiement de votre commande {commande}",
                source=token_stripe
            )
            commande = paiement(
                Produit = commande,
                id_utilisateur = recup_id,
                id_stripe = creer_charge.id,
                date_paiement= datetime.now()
            )
            commande.save()

            send_mail(
                "confirmation de paiement",f"le paiement de votre commande {commande} avec un montant de : {prix_finale}",settings.EMAIL_HOST_USER,[email_client],fail_silently=False
            )
            return render(request,'procedure_paiement.html',{"message":"paiement réussi"})
        except stripe.error.StripeError as message :
            return render(request,'procedure_paiement.html',{"erreur":message})
    return render(request,'procedure_paiement.html')
        
#facture
def affiche_facture(request):
    date = datetime.now()
    return render(request,"facture.html",{"date":date})

#creation factiure

# def telecharge(request):
#     facture = render_to_string("facture.html")

#     html = HTML(string=facture)

#     generer = html.write_pdf()
#     pdf_fichier = HttpResponse(generer,content_type = "application/pdf")
#     pdf_fichier["Content-Disposition"] = "attachement;filename = 'facture.pdf'"

#     return pdf_fichier



# def telecharge(request):
#     # Create a file-like buffer to receive PDF data.
#     facture = render_to_string("facture.html")

#     buffer = io.BytesIO()

#     # Create the PDF object, using the buffer as its "file."
#     p = canvas.Canvas(buffer)

#     # Draw things on the PDF. Here's where the PDF generation happens.
#     # See the ReportLab documentation for the full list of functionality.
#     p.drawString(10,10, facture)

#     # Close the PDF object cleanly, and we're done.
#     p.showPage()
#     p.save()

#     # FileResponse sets the Content-Disposition header so that browsers
#     # present the option to save the file.
#     buffer.seek(0)
#     return FileResponse(buffer, as_attachment=True, filename="hello.pdf")

# def telecharge(request):
#     facture = render_to_string("facture.html")

#     generer = PDFTemplateView.as_view(template_name=facture,filename='my_pdf.pdf')
#     pdf_fichier = HttpResponse(generer,content_type = "application/pdf")
#     # pdf_fichier["Content-Disposition"] = "attachement;filename = facture.pdf"

#     return pdf_fichier
def telecharge(request):
    pass

