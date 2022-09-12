from django.db import models
from django.shortcuts import render, redirect
from .models import Idioma
from django.http import HttpResponse
from .models import *
from .forms import *


def home(request):
    return render(request, 'dashboard.html')


def idiomas(request):
    idiomas = Idioma.objects.all()
    return render(request, 'idiomas.html', {'idiomas': idiomas})


def capacitaciones(request):
    capacitaciones = Capacitaciones.objects.all()
    return render(request, 'capacitaciones.html')


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
        # print('Printing POST: ', request.POST)
        form = IdiomaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/idiomas')

    context = {'form': form}
    return render(request, 'idiomasForm.html', context)


def updateIdioma(request, pk):
    idioma = Idioma.objects.get(id=pk)
    form = IdiomaForm(instance=idioma)

    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = IdiomaForm(request.POST, instance=idioma)
        if form.is_valid():
            form.save()
            return redirect('/idiomas')

    context = {'form': form}
    return render(request, 'idiomasForm.html', context)

def deleteIdioma(request, pk):
    idioma = Idioma.objects.get(id=pk)
    if request.method == "POST":
        idioma.delete()
        return redirect('/idiomas')
    context = {'item': idioma}
    return render(request, 'delete.html', context)

def createCapacitaciones(request):
    form = CapacitacionesForm()

    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = CapacitacionesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/capacitaciones')

    context = {'form': form}
    return render(request, 'capacitacionesForm.html', context)


def updateCapacitaciones(request, pk):
    capacitaciones = Capacitaciones.objects.get(id=pk)
    form = CapacitacionesForm(instance=capacitaciones)

    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = CapacitacionesForm(request.POST, instance=capacitaciones())
        if form.is_valid():
            form.save()
            return redirect('/capacitaciones')

    context = {'form': form}
    return render(request, 'capacitacionesForm.html', context)

def deleteCapacitaciones(request, pk):
    capacitaciones = Capacitaciones.objects.get(id=pk)
    if request.method == "POST":
        capacitaciones.delete()
        return redirect('/idiomas')
    context = {'item': capacitaciones}
    return render(request, 'delete.html', context)


def createCompetencias(request):
    form = CompetenciaForm()

    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = CompetenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/competencia')

    context = {'form': form}
    return render(request, 'competenciaForm.html', context)


def updateCompetencia(request, pk):
    competencia = Competencia.objects.get(id=pk)
    form = CompetenciaForm(instance=capacitaciones)

    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = CompetenciaForm(request.POST, instance=competencia())
        if form.is_valid():
            form.save()
            return redirect('/competencia')

    context = {'form': form}
    return render(request, 'competenciaForm.html', context)

def deleteCompetencia(request, pk):
    competencia = Competencia.objects.get(id=pk)
    if request.method == "POST":
        competencia.delete()
        return redirect('/idiomas')
    context = {'item': competencia}
    return render(request, 'delete.html', context)
