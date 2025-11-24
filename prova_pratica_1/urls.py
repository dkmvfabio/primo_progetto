from django.urls import path
from prova_pratica_1.views import index3, diff, pari


app_name = "prova_pratica_1"
urlpatterns=[
    path('index3', index3, name='index3'),
    path('diff', diff, name='diff'),
    path('pari', pari, name='pari')
]