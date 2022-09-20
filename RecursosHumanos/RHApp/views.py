from django.db import models
from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
import csv
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
import datetime

# CSV Generator
def exportCSV(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Empleados.csv'

    writer = csv.writer(response)
    writer.writerow(['Cedula','Nombre','Fecha Ingreso', 'Departamento', 'Salario Mensual', 'Puesto', 'Estado'])

    empleados = Empleados.objects.all()

    for empleado in empleados:
        writer.writerow([empleado.Cedula, empleado.Nombre, empleado.Fecha_Ingreso, empleado.Departamento, empleado.SalarioMensual, empleado.Puesto, empleado.Activo])

    return response

def CandidatosProcess(request, pk):
    #Recibe el ID del registro seleccionado y almacena su informacion dentro de la variable creada
    candidato = Candidatos.objects.filter(id=pk)

    #Explora cada campo del modelo candidato y lo inserta en los campos de Empleado asignados
    for cnd in candidato:
        Empleados.objects.create(Cedula=cnd.Cedula, Nombre=cnd.Nombre, Fecha_Ingreso=datetime.datetime.now(), Departamento=cnd.Departamento, SalarioMensual=cnd.SalarioAspirado, Puesto=cnd.PuestoAspira, Activo=True)

    #Elimina el Candidato seleccionado
    Candidatos.objects.filter(id=pk).delete()
    return redirect('/empleados')

def home(request):
    return render(request, 'dashboard.html')

def idiomas(request):
    idiomas = Idioma.objects.all()
    return render(request, 'idiomas.html', {'idiomas': idiomas})

def capacitaciones(request):
    capacitaciones = Capacitaciones.objects.all()
    return render(request, 'capacitaciones.html', {'capacitaciones': capacitaciones})


def competencia(request):
    competencia = Competencia.objects.all()
    return render(request, 'competencia.html', {'competencia': competencia})

def puesto(request):
    puesto = Puesto.objects.all()
    return render(request, 'puesto.html', {'puesto': puesto})

def experienciaLaboral(request):
    experienciaLaboral = ExperienciaLaboral.objects.all()
    return render(request, 'expLaboral.html', {'experienciaLaboral': experienciaLaboral})

def empleados(request):
    empleados = Empleados.objects.all()
    return render(request, 'empleados.html', {'empleados': empleados})

def candidatos(request):
    candidatos = Candidatos.objects.all()
    return render(request, 'candidatos.html', {'candidatos': candidatos})

def candidatosSelection(request):
    Candidato = Candidatos.objects.all()
    return render(request, 'CandidatosSelection.html', {'Candidato': Candidato})

#Idiomas (Modelo)

def createIdioma(request):
    form = IdiomaForm()

    if request.method == "POST":
        print('Printing POST: ', request.POST)
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
        print('Printing POST: ', request.POST)
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

#Capacitaciones (Modelo)

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

# Competencias (Modelo)

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
        return redirect('/competencia')
    context = {'item': competencia}
    return render(request, 'delete.html', context)

#Puesto (Model)

def createPuesto(request):
    form = PuestoForm()

    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = PuestoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/puesto')

    context = {'form': form}
    return render(request, 'puestoForm.html', context)

def updatePuesto(request, pk):
    puesto = Puesto.objects.get(id=pk)
    form = PuestoForm(instance=puesto)

    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = PuestoForm(request.POST, instance=puesto)
        if form.is_valid():
            form.save()
            return redirect('/puesto')

    context = {'form': form}
    return render(request, 'puestoForm.html', context)

def deletePuesto(request, pk):
    puesto = Puesto.objects.get(id=pk)
    if request.method == "POST":
        puesto.delete()
        return redirect('/puesto')
    context = {'item': puesto}
    return render(request, 'delete.html', context)

# Experiencia Laboral
def createExpLaboral(request):
    form = ExpLabForm()

    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = ExpLabForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/explaboral')

    context = {'form': form}
    return render(request, 'expLabForm.html', context)

def updateExpLaboral(request, pk):
    experienciaLaboral = ExperienciaLaboral.objects.get(id=pk)
    form = ExpLabForm(instance=experienciaLaboral)

    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = ExpLabForm(request.POST, instance=experienciaLaboral)
        if form.is_valid():
            form.save()
            return redirect('/explaboral')

    context = {'form': form}
    return render(request, 'expLabForm.html', context)

def deleteExpLaboral(request, pk):
    experienciaLaboral = ExperienciaLaboral.objects.get(id=pk)
    if request.method == "POST":
        experienciaLaboral.delete()
        return redirect('/explaboral')
    context = {'item': experienciaLaboral}
    return render(request, 'delete.html', context)

def createCandidatos(request):
    form = CandidatosForm()

    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = CandidatosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/candidatos')

    context = {'form': form}
    return render(request, 'candidatosForm.html', context)

def updateCandidatos(request, pk):
    candidatos = Candidatos.objects.get(id=pk)
    form = CandidatosForm(instance=candidatos)

    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = CandidatosForm(request.POST, instance=candidatos)
        if form.is_valid():
            form.save()
            return redirect('/candidatos')

    context = {'form': form}
    return render(request, 'candidatosForm.html', context)

def deleteCandidatos(request, pk):
    candidatos = Candidatos.objects.get(id=pk)
    if request.method == "POST":
        candidatos.delete()
        return redirect('/candidatos')
    context = {'item': candidatos}
    return render(request, 'delete.html', context)

def createEmpleados(request):
    form = EmpleadosForm()

    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = EmpleadosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/empleados')

    context = {'form': form}
    return render(request, 'empleadosForm.html', context)

def updateEmpleados(request, pk):
    empleados = Empleados.objects.get(id=pk)
    form = EmpleadosForm(instance=empleados)

    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = EmpleadosForm(request.POST, instance=empleados)
        if form.is_valid():
            form.save()
            return redirect('/empleados')

    context = {'form': form}
    return render(request, 'empleadosForm.html', context)

def deleteEmpleados(request, pk):
    empleados = Empleados.objects.get(id=pk)
    if request.method == "POST":
        empleados.delete()
        return redirect('/empleados')
    context = {'item': empleados}
    return render(request, 'deleteEmpleados.html', context)

# User Login
def loginView(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'El Usuario o la Contraseña no es correcto')

    context = {}
    return render(request, 'login.html', context)

def logoutView(request):
    logout(request)
    return redirect('login')

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'La cuenta' + user + 'ha sido creada')

            return redirect('login')

    context = {'form':form}
    return render(request, 'register.html', context)
