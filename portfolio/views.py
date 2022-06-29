
from django.shortcuts import render
from .models import Project
from portfolio.forms import FormularioPortafolio
from django.db.models import Q

# Create your views here.

def home(request):
    queryset = request.GET.get("buscar")
    print(queryset)
    projects = Project.objects.filter()
    if queryset:
        projects = Project.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()

    return render(request, 'home.html', {'projects' : projects})



def proyectosForm(request):

    if request.method == 'POST':

        miFormulario = FormularioPortafolio(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            project = Project(titulo = informacion['proyecto'], descripcion=informacion['descripcion'], imagen=informacion['imagen'] ,url=informacion['url'])
            project.save()

            return render(request, 'home.html')

    else:
        miFormulario= FormularioPortafolio()
    return render(request, 'formulario_port.html', {'miFormulario':miFormulario})

