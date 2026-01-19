from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Articolo, Giornalista

"""
Salviamo gli articoli e i giornalisti come unica stringa 
def home(request):
    a = ""
    g = ""
    for art in Articolo.objects.all():
        a += (art.titolo + "<br>")

    for gio in Giornalista.objects.all():
        g += (gio.nome + "<br>")
    response = "Articoli:<br>" + a + "<br>Giornalisti:<br>" + g

    return HttpResponse("<h1>" + response + "</h1>")
"""

"""
Salviamo articoli e giornalisti dentro delle liste
def home(request):
    a = []
    g = []
    for art in Articolo.objects.all():
        a.append(art.titolo)

    for gio in Giornalista.objects.all():
        g.append(gio.nome)

    response = str(a) + "<br>" + str(g)
    print(response)

    return HttpResponse("<h1>" + response + "</h1>")
"""

def index4(request):
    return render(request,"news/index4.html")

"""Salviamo gli articoli e i giornalisti come degli oggetti"""
def home(request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()

    context = {"articoli": articoli, "giornalisti": giornalisti}
    print(context)

    return render(request, "homepage.html", context)

def articoloDetailView(request, pk):
    # articolo = Articolo.objects.get(pk=pk)
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {"articolo": articolo}
    return render(request, "articolo_detail.html", context)

def listaArticoli(request, pk=None):
    trovato = False
    is_vuota = False
    if pk:
        articoli = Articolo.objects.filter(giornalista_id=pk)
        trovato = True
    else:
        articoli = Articolo.objects.all()
    if not articoli:
        is_vuota = True
    context={
        'articoli': articoli,
        'trovato': trovato,
        'is_vuota': is_vuota
    }   
    return render(request, 'lista_articoli.html', context)
