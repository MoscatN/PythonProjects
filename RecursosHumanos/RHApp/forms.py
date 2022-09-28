from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class IdiomaForm(ModelForm):
    class Meta:
        model = Idioma
        fields = ['Idioma', 'Activo']

    Idioma = forms.CharField()
    Activo = forms.BooleanField()


class CapacitacionesForm(ModelForm):

    class Meta:
        model = Capacitaciones
        fields = ['Descripcion', 'Nivel', 'Fecha_Desde', 'Fecha_Hasta', 'Institucion']

    Descripcion = forms.CharField()
    Fecha_Desde = forms.DateField(widget=DateInput)
    Fecha_Hasta = forms.DateField(widget=DateInput)
    Institucion = forms.CharField()

class CompetenciaForm(ModelForm):
    class Meta:
        model = Competencia
        fields = ['Descripcion', 'Activo']

    Descripcion = forms.CharField()
    Activo = forms.BooleanField()

class PuestoForm(ModelForm):
    class Meta:
        model = Puesto
        fields = ['Puesto', 'Riesgo', 'SalarioMinimo', 'SalarioMaximo', 'Activo']

    Puesto = forms.CharField()
    SalarioMinimo = forms.IntegerField()
    SalarioMaximo = forms.IntegerField()

class ExpLabForm(ModelForm):
    class Meta:
        model = ExperienciaLaboral
        fields = ['Empresa', 'PuestoOcupado', 'Fecha_Desde', 'Fecha_Hasta', 'Salario']

    Empresa = forms.CharField()
    PuestoOcupado = forms.CharField()
    Fecha_Desde = forms.DateField(widget=DateInput)
    Fecha_Hasta = forms.DateField(widget=DateInput)
    Salario = forms.IntegerField()

class CandidatosForm(ModelForm):
    class Meta:
        model = Candidatos
        fields = ['Cedula', 'Nombre', 'PuestoAspira', 'Departamento', 'SalarioAspirado', 'CompetenciasPrincipales', 'CapacitacionesPrincipales', 'Exp_Laboral', 'RecomendadoPor']

    Cedula = forms.CharField()
    Nombre = forms.CharField()
    PuestoAspira = forms.ModelChoiceField(queryset=Puesto.objects.all(), initial=0)
    CompetenciasPrincipales = forms.ModelMultipleChoiceField(
        queryset=Competencia.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    CapacitacionesPrincipales = forms.ModelMultipleChoiceField(
        queryset=Capacitaciones.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    Exp_Laboral = models.ForeignKey(ExperienciaLaboral, on_delete=models.CASCADE)
    RecomendadoPor = models.CharField

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Exp_Laboral.queryset = ExperienciaLaboral.objects.none()

class EmpleadosForm(ModelForm):
    class Meta:
        model = Empleados
        fields = ['Cedula', 'Nombre', 'Fecha_Ingreso', 'Departamento', 'SalarioMensual', 'Puesto', 'Activo']

    Cedula = forms.CharField()
    Nombre = forms.CharField()
    Fecha_Ingreso = forms.DateField(widget=DateInput)
    Departamento = forms.CharField()
    SalarioMensual = forms.IntegerField()
    Puesto = forms.ModelChoiceField(queryset=Puesto.objects.all(), initial=0)
    Activo = forms.BooleanField()
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
