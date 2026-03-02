from django.shortcuts import render, HttpResponse
from .forms import FormContatto, Contatto
# Create your views here.
def contatti(request):

    # Se la richiesta è di tipo POST, allora possiamo processare i dati
    if request.method == "POST":

        # Creiamo l'istanza del form e la popoliamo con i dati della POST request (processo di "binding")
        form = FormContatto(request.POST)

        # is_valid() controlla se il form inserito è valido:
        if form.is_valid():
            # a questo punto possiamo usare i dati validi:
            # tenere a mente che cleaned_data["nome_dato"] ci permette di accedere ai dati validati e convertiti in tipi standard di Python
            print("Salvo il contatto nel database")
            nuovo_contatto = form.save()
            print("new_post: ", nuovo_contatto)
            print(nuovo_contatto.nome)
            print(nuovo_contatto.cognome)
            print(nuovo_contatto.email)
            print(nuovo_contatto.contenuto)

            # ringrazio l'utente per averci contattato - volendo possiamo efettuare un redirect a una pagina specifica
            return HttpResponse("<h1>Grazie per averci contattato!</h1>")

    # Se la richiesta HTTP usa il metodo GET o qualsiasi altro metodo, allora creo il form di default vuoto
    else:
        form = FormContatto()

    context = {"form": form}
    return render(request, "contatto.html", context)

def listaContatti(request):
    contatti = Contatto.objects.all()
    context = {
        "contatti": contatti
    }
    return render(request, "lista_contatti.html", context)