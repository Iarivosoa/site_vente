from django.contrib import admin
from .models import insertion_produit
# Register your models here.
class affiche_produit(admin.ModelAdmin):
    list_display = ("nom","description","prix","photo","type")
admin.site.register(insertion_produit,affiche_produit)