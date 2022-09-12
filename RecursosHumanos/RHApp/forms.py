from django.forms import ModelForm
from .models import *

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
        fields = '__all__'

class EmpleadosForm(ModelForm):
    class Meta:
        model = Empleados
        fields = '__all__'