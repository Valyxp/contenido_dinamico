from django.shortcuts import render


# Create your views here.
def lista_empleados(request):
    empleados = ["Emilio", "Miguel", "Oscar", "Victor", "Ivan"]
    return render(request, "empleados/lista_empleados.html", {"empleados": empleados})
