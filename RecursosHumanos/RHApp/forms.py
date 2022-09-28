from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class IdiomaForm(ModelForm):
    class Meta:
        model = Idioma
        fields = '__all__'

class CapacitacionesForm(ModelForm):
    class Meta:
        model = Capacitaciones
        fields = '__all__'

class CompetenciaForm(ModelForm):
    class Meta:
        model = Competencia
        fields = '__all__'

class PuestoForm(ModelForm):
    class Meta:
        model = Puesto
        fields = '__all__'

class ExpLabForm(ModelForm):
    class Meta:
        model = ExperienciaLaboral
        fields = '__all__'

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
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']