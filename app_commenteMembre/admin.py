from django.contrib import admin
from .models import CommenteMembre
# Register your models here.
class affiche_commente(admin.ModelAdmin):
    list_display = ("id_pro","id_membre","commentaire","date")
admin.site.register(CommenteMembre,affiche_commente)