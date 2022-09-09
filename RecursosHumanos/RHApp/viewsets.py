from rest_framework import viewsets
from RHApp.models import Idioma, Competencia, Capacitaciones,Puesto,Candidatos, ExperienciaLaboral, Empleados
from RHApp.serializers import IdiomaSerializer, CompetenciaSerializer, CapacitacionesSerializer, PuestoSerializer, CandidatosSerializer, Exp_LaboralSerializer, EmpleadosSerializer

class IdiomaViewSet(viewsets.ModelViewSet):
    serializer_class = IdiomaSerializer

    def get_queryset(self):
        return Idioma.objects.all()

class CompetenciaViewSet(viewsets.ModelViewSet):
    serializer_class = CompetenciaSerializer

    def get_queryset(self):
        return Competencia.objects.all()

class CapacitacionesViewSet(viewsets.ModelViewSet):
    serializer_class = CapacitacionesSerializer

    def get_queryset(self):
        return Capacitaciones.objects.all()

class PuestoViewSet(viewsets.ModelViewSet):
    serializer_class = PuestoSerializer

    def get_queryset(self):
        return Puesto.objects.all()

class CandidatosViewSet(viewsets.ModelViewSet):
    serializer_class = IdiomaSerializer

    def get_queryset(self):
        return Idioma.objects.all()

class Exp_LaboralViewSet(viewsets.ModelViewSet):
    serializer_class = Exp_LaboralSerializer

    def get_queryset(self):
        return ExperienciaLaboral.objects.all()

class EmpleadosViewSet(viewsets.ModelViewSet):
    serializer_class = EmpleadosSerializer

    def get_queryset(self):
        return Empleados.objects.all()