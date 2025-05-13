from django.contrib import admin
from .models import Insertion_membre
# Register your models here.
class affiche_membre(admin.ModelAdmin):
    list_display = ("nom","prenom","email","mot_de_passe","photo")
admin.site.register(Insertion_membre,affiche_membre)