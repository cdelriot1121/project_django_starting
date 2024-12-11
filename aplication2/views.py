from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Respuesta(request):
    path = request.path
    response = HttpResponse("Esta es una respuesta HttpResponse")
    return response


def bebidaItems(request, bebida):
    items = {
        'cafe': 'cafe es una bebida del mundo para mantenerte activo y es muy rico',
        'cerveza': 'La cerveza es una bebida para disfrutar con amigos y familia',
    }

    descripcion = items[bebida]

    return HttpResponse(f"<h2> {bebida} </h2>" + descripcion)