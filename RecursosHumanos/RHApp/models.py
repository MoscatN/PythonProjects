from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

class Idioma(models.Model):
    """RHApp manejados por el candidato"""

    Idioma = models.CharField(max_length=200)
    Activo = models.BooleanField()

    def __str__(self):
        """"""
        return self.Idioma

class Capacitaciones(models.Model):
    """"""

    Descripcion = models.CharField(max_length=200)
    Nivel = models.CharField(max_length= 15)
    Fecha_Desde = models.DateField(auto_now_add= False, null=True)
    Fecha_Hasta = models.DateField(auto_now_add= False, null=True)
    Institucion = models.CharField(max_length=55, null=True)

    def __str__(self):
        return self.Descripcion

class Competencia(models.Model):
    """Competencias del Candidato"""
    Descripcion = models.CharField(max_length=200)
    Activo = models.BooleanField()

    def __str__(self):
        """Retorna una cadena en representacion del modelo"""
        return self.Descripcion

class Puesto(models.Model):
    """"""
    # class Riesgo(models.TextChoices):
    #     Alto = 'H', _('Alto')
    #     Medio = 'M', _('Medio')
    #     Bajo = 'L', _('Bajo')

    Puesto = models.TextField(max_length=50)

    Riesgo = models.CharField(max_length=20)

    SalarioMinimo = models.IntegerField(null=True)

    SalarioMaximo = models.IntegerField(null=True)

    Activo = models.BooleanField()

    def __str__(self):
        return self.Puesto

class ExperienciaLaboral(models.Model):

    Empresa = models.TextField(max_length=35)

    PuestoOcupado = models.TextField(max_length=45)

    Fecha_Desde = models.DateField(auto_now_add=False, null=True)

    Fecha_Hasta = models.DateField(auto_now_add=False, null=True)

    Salario = models.IntegerField

    def __str__(self):
        return self.PuestoOcupado

class Candidatos(models.Model):
    """"""
    Cedula = models.CharField(
        max_length=13,

        validators=[
            RegexValidator(
                regex='^\d{3}-\d{7}-\d{1}$',
                message='El formato de Cedula debe ser XXX-XXXXXXX-X (Solo numerico)'
            )
        ]
    )
    Nombre = models.CharField(max_length=25)
    PuestoAspira = models.ForeignKey(
        Puesto,
        on_delete=models.CASCADE,
        )
    Departamento = models.CharField(max_length=50)
    SalarioAspirado = models.IntegerField
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

    def __str__(self):
        return self.Nombre

class Empleados(models.Model):

    Cedula = models.TextField(
        max_length=13,
        validators=[
            RegexValidator(
                regex='^\d{3}-\d{7}-\d{1}$',
                message='El formato de Cedula debe ser XXX-XXXXXXX-X (Solo numerico)'
            )
        ]
    )

    Nombre = models.TextField(max_length=25)

    Fecha_Ingreso = models.DateField(auto_now_add=False, null=True)

    Departamento = models.TextField(max_length=30)

    Puesto = models.ForeignKey(
        Puesto,
        on_delete= models.CASCADE
    )
    SalarioMensual = models.IntegerField

    Activo = models.BooleanField()

    def __str__(self):
        return self.Nombre