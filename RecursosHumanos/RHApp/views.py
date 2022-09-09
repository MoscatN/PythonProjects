from django.db import models
from django.shortcuts import render
from .models import Idioma
from django.http import HttpResponse
from .models import *

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


# def create_view(request):
#     """Home page for RHApp model"""
#     context ={}
#
#     form = IdiomasForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#
#     context['form'] = form
#     return render(request, 'create_view.html', context)