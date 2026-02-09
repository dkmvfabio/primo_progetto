from django.urls import path
from voti.views import index5, listaMaterie, votiStudenti, mediaStudenti, datiStudenti

 


app_name = "voti"
urlpatterns=[
    path('index5', index5, name='index5'),
    path('listaMaterie', listaMaterie, name='listaMaterie'),
    path('votiStudenti', votiStudenti, name='votiStudenti'),
    path('mediaStudenti', mediaStudenti, name='mediaStudenti'),
    path('datiStudenti', datiStudenti, name='datiStudenti'),
]