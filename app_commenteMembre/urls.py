from django.urls import path
from .views import*

urlpatterns =[
    path("commentaire",commentaire,name="commentaire"),
    path("suppression_commente/<int:id_commente>",suppression_commente,name="suppression_commente")
]