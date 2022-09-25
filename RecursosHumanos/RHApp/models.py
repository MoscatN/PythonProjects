import datetime

from django.core.exceptions import ValidationError
from django.db import models
from .ValidacionCedula import validarCedula
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.utils import timezone

class Idioma(models.Model):
    """RHApp manejados por el candidato"""

    Idioma = models.CharField(max_length=200, unique=True)
    Activo = models.BooleanField()

    def __str__(self):
        """"""
        return self.Idioma

class Capacitaciones(models.Model):
    """"""
    GRADO = 'Grado'
    POSTGRADO = 'Post-Grado'
    MAESTRIA = 'Maestria'
    DOCTORADO = 'Doctorado'
    TECNICO = 'Tecnico'
    GESTION = 'Gestion'
    Nivel = [
       (GRADO, 'Grado'),
       (POSTGRADO, 'Post-Grado'),
       (MAESTRIA, 'Maestria'),
       (DOCTORADO, 'Doctorado'),
       (TECNICO, 'Tecnico'),
       (GESTION, 'Gestion'),
     ]

    Descripcion = models.CharField(max_length=200, blank=False)
    Nivel = models.CharField(
        max_length=15,
        choices=Nivel,
        default=GRADO)
    Fecha_Desde = models.DateField(auto_now_add= False, null=True)
    Fecha_Hasta = models.DateField(auto_now_add= False, null=True)
    Institucion = models.CharField(max_length=55, null=True)

    def __str__(self):
        return self.Descripcion

class Competencia(models.Model):
    """Competencias del Candidato"""
    Descripcion = models.CharField(max_length=200, unique=True)
    Activo = models.BooleanField()

    def __str__(self):
        """Retorna una cadena en representacion del modelo"""
        return self.Descripcion

class Puesto(models.Model):
    """"""
    ALTO = 'Alto'
    MEDIO = 'Medio'
    BAJO = 'Bajo'

    Riesgo = [
        (ALTO, 'Alto'),
        (MEDIO, 'Medio'),
        (BAJO, 'Bajo')
    ]

    Puesto = models.CharField(max_length=50)

    Riesgo = models.CharField(max_length=20, choices=Riesgo)

    SalarioMinimo = models.IntegerField(null=True, validators=[MinValueValidator(0)])

    SalarioMaximo = models.IntegerField(null=True, validators=[MinValueValidator(0)])

    Activo = models.BooleanField()

    def __str__(self):
        return self.Puesto

    def clean(self):
        if self.SalarioMaximo <= self.SalarioMinimo:
            raise ValidationError(
                {'SalarioMaximo': "El Salario Maximo no puede ser igual al minimo"}
            )

class ExperienciaLaboral(models.Model):

    Empresa = models.CharField(max_length=35)

    PuestoOcupado = models.CharField(max_length=45)

    Fecha_Desde = models.DateField(auto_now_add=False, null=True )

    Fecha_Hasta = models.DateField(auto_now_add=False, null=True)

    Salario = models.IntegerField(validators=[MinValueValidator(0)])

    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False)

    def __str__(self):
        return self.PuestoOcupado

    #Validacion que no permite fechas mas recientes que la fecha de hoy
    def clean(self, *args, **kwargs):
        # run the base validation
        super(ExperienciaLaboral, self).clean(*args, **kwargs)

        if self.Fecha_Desde > datetime.date.today():
            raise ValidationError(
                {'Fecha_Desde': 'La ingresada no puede ser mas reciente que el dia de hoy.'})

        if self.Fecha_Hasta > datetime.date.today():
            raise ValidationError(
                {'Fecha_Hasta': 'La fecha ingresada no es correcta.'})
        if self.Fecha_Hasta < self.Fecha_Desde:
            raise ValidationError(
                {'Fecha_Hasta': 'La fecha ingresada no puede ser menor a la inicial.'})


class Candidatos(models.Model):
    """"""
    Cedula = models.CharField(max_length=13)
    Nombre = models.CharField(max_length=25)
    PuestoAspira = models.ForeignKey(
        Puesto,
        on_delete=models.CASCADE,
        )
    Departamento = models.CharField(max_length=50)
    SalarioAspirado = models.IntegerField(validators=[MinValueValidator(0)])
    CompetenciasPrincipales = models.ForeignKey(
        Competencia,
        on_delete=models.CASCADE
    )
    CapacitacionesPrincipales = models.ForeignKey(
        Capacitaciones,
        on_delete=models.CASCADE
    )
    Exp_Laboral = models.ForeignKey(
        ExperienciaLaboral,
        on_delete=models.CASCADE
    )
    RecomendadoPor = models.CharField(max_length=50)

    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False)
    def __str__(self):
        return self.Nombre

    def clean(self):
        if validarCedula(self.Cedula) == False:
            raise ValidationError(
                {'Cedula': "La cedula ingresada es incorrecta"}
            )

    # def ToArchive(self):
    #     from django.db import connection, transaction
    #     cursor = connection.cursor()
    #     cursor.execute("Insert Into Empleados")
    #     transaction.commit_unless_managed()
    #     self.delete()

class Empleados(models.Model):

    Cedula = models.CharField(max_length=13, unique=True)

    Nombre = models.CharField(max_length=25)

    Fecha_Ingreso = models.DateField(auto_now_add=False, null=True)

    Departamento = models.CharField(max_length=30)

    SalarioMensual = models.IntegerField(validators=[MinValueValidator(0, message="El salario debe ser mayor que cero")], null=True)

    Puesto = models.ForeignKey(
        Puesto,
        on_delete= models.CASCADE
    )

    Activo = models.BooleanField()

    def __str__(self):
        return self.Nombre

    def clean(self):
        if validarCedula(self.Cedula) == False:
            raise ValidationError(
                {'Cedula': "La cedula ingresada es incorrecta"}
            )
