from django.urls import path
from.views import home, articoloDetailView, index4, listaArticoli

app_name = 'news'

urlpatterns = [
    path('index4', index4, name='index4'),
    path('', home, name="homeview"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path('lista_articoli', listaArticoli, name="lista_articoli")
]