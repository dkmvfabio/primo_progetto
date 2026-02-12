from django.shortcuts import render

def index5(request):
    return render(request,"voti/index5.html")

def listaMaterie(request):
    context = {
        'materie' : ["Matematica","Italiano","Inglese","Storia","Geografia"]
    }
    return render(request,"voti/lista_materie.html", context)

def votiStudenti(request):
    context = {
        'voti' : {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
                'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
                'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}    
        }
    return render(request,"voti/voti_studenti.html", context)

def mediaStudenti(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    
    medieVoti = {}
    for studente, voti in voti.items():
        sommaVoti = 0
        i = 0
        for materia, voto, assenza in voti:
            sommaVoti += voto
            i += 1
       
        medieVoti[studente]=sommaVoti/i

    context = {
        'medieVoti': medieVoti
    }
    return render(request,"voti/media_voti.html", context)

def datiStudenti(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    
    votoMax = 0
    materieMax = []
    studentiMax =  []

    votoMin = 100
    materieMin = []
    studentiMin =  []
    for studente, dati in voti.items():
        for materia, voto, assenza in dati:
            if voto > votoMax:
                votoMax = voto
            if voto < votoMin:
                votoMin = voto

    for studente, voti in voti.items():
        for materia, voto, assenza in voti:
            if voto == votoMax:
                materieMax.append(materia)
                studentiMax.append(studente)
            if voto == votoMin:
                materieMin.append(materia)
                studentiMin.append(studente)
       

    context = {
        'votoMax': votoMax,
        'materieMax' : materieMax,
        'studentiMax' : studentiMax,
        'votoMin': votoMin,
        'materieMin' : materieMin,
        'studentiMin' : studentiMin
    }
    return render(request,"voti/dati_studenti.html", context)