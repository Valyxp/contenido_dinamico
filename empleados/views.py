from django.shortcuts import render


# Create your views here.
def lista_empleados(request):
    empleados = ["Ana", "Luis", "Pedro", "María", "Carmen"]
    return render(request, "empleados/lista_empleados.html", {"empleados": empleados})
