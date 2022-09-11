from django.db import models
from django.shortcuts import render, redirect
from .models import Idioma
from django.http import HttpResponse
from .models import *
from .forms import IdiomaForm

def home(request):
    return render(request, 'dashboard.html')

def idiomas(request):
    idiomas = Idioma.objects.all()
    return render(request, 'idiomas.html', {'idiomas':idiomas})

def capacitaciones(request):
    return render(request,'capacitaciones.html')

def competencia(request):
    return render(request, 'competencia.html')

def puesto(request):
    return render(request, 'puesto.html')

def experienciaLaboral(request):
    return render(request, 'explaboral.html')

def empleados(request):
    return render(request, 'empleados.html')

def candidatos(request):
    return render(request, 'candidatos.html')

def createIdioma(request):

    form = IdiomaForm()

    if request.method == 'POST':
        #print('Printing POST: ', request.POST)
        form = IdiomaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'idiomasForm.html', context)

