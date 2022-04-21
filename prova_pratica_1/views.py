from django.http import JsonResponse
from django.shortcuts import render


def listaMaterie(request):
    materie={
        'm1':"Matematica",
        'm2':"Italiano",
        'm3':"Inglese",
        'm4':"Storia",
        'm5':"Geografia"
    }
    data = {"materie": list(materie.values("pk", "name"))}
    response= JsonResponse(data)
    return response

def materie_detail(request, pk):
    try: 
        materia=listaMaterie.objects.get(pk=pk)
        data={"materia": {
            "name": materia.name
        }}
        response=JsonResponse(data)
    except listaMaterie.doesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "prodotto non trovato"
            }},
            status=404)
    return response

def view_b(request):
    materie={
        'm1':"Matematica",
        'm2':"Italiano",
        'm3':"Inglese",
        'm4':"Storia",
        'm5':"Geografia"
    }
    return render(request,"view_b.html",materie)

def view_c(request):
    context={
        'GiuseppeGullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7.5,4),("Storia",7.5,4),("Geografia",5,7)],
        'AntonioBarbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9.5,0),("Storia",8,2),("Geografia",8,1)],
        'NicolaSpina':[("Matematica",7.5,2),("Italiano",6,2),("Inglese",4,3),("Storia",8.5,2),("Geografia",8,2)]
        }
    return render(request, "view_c.html", context)