
from django.shortcuts import render
from .models import Project
from portfolio.forms import FormularioPortafolio

# Create your views here.

def home(request):
    projects = Project.objects.all()


    return render(request, 'home.html', {'projects' : projects})

def formulario_portfolio(request):

    if request.method == 'POST':

        miFormulario = FormularioPortafolio(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion - miFormulario.cleaned_data

            proyec = Project(proyecto = informacion['proyecto'], descripcion=informacion['descripcion'], url=informacion['url'])
            proyec.save()

            return render(request, 'home.html')

    else:
        miFormulario= FormularioPortafolio()
    return render(request, 'formulario_port.html', {'miFormulario':miFormulario})