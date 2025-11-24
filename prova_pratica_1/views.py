from django.shortcuts import render
import random
def index3(request):
    return render(request,"prova_pratica_1/index3.html")

def diff(request):
    numero1 = random.randint(1,20)
    numero2 = random.randint(1,20)
    if(numero1>numero2):
        differenza = numero1 - numero2
    elif(numero1<numero2):
        differenza = numero2 - numero1
    else:
        differenza = 0
    context={
        'numero1' : numero1,
        'numero2' : numero2,
        'differenza' : differenza
    }
    return render(request, "prova_pratica_1/diff.html", context)

def pari(request):
    lista = []
    contaPari = 0
    contaDispari = 0
    x = 0
    while(x<15):
        numero = random.randint(1,20)
        if((numero%2)==0):
            contaPari+=1
        else:
            contaDispari+=1
        lista.append(numero)
        x+=1

    context={
        'lista' : lista,
        'contaPari' : contaPari,
        'contaDispari' : contaDispari
    }
    return render(request, "prova_pratica_1/pari.html", context)