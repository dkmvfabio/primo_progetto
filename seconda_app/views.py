from django.shortcuts import render
def index(request):
    return render(request,"seconda_app/index.html")

def es_if(request):
    context={
        'var1' : 200,
        'var2' : 200,
        'var3' : 300
    }
    return render(request, "seconda_app/es_if.html", context)

def if_else_elif(request):
    context = {
        'var1' : 100,
        'var2' : 100.0,
        'var3' : 100.50,
    }
    return render(request, "seconda_app/if_else_elif.html", context)
