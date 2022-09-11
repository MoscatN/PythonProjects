from django.forms import ModelForm
from .models import Idioma

class IdiomaForm(ModelForm):
    class Meta:
        model = Idioma
        fields = '__all__'