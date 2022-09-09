from rest_framework import serializers
from RHApp.models import Idioma

class IdiomaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = ['id', 'Idioma', 'Activo']

# class CompetenciaSerializer (serializers.ModelSerializer):
#     class Meta:
#         model = Competencia
#         fields = ['id', 'Descripcion', 'Activo']
#
# class CapacitacionesSerializer (serializers.ModelSerializer):
#     class Meta:
#         model = Capacitaciones
#         fields = ['id', 'Descripcion', 'Activo']
#
# class PuestoSerializer (serializers.ModelSerializer):
#     class Meta:
#         model = Puesto
#         fields = ['id', 'Puesto','Riesgo','SalarioMinimo','SalarioMaximo' ,'Activo']
#
# class CandidatosSerializer (serializers.ModelSerializer):
#     class Meta:
#         model = Candidatos
#         fields = ['id', 'Cedula','Nombre' ,'PuestoAspira','Departamento','SalarioAspirado','CompetenciasPrincipales','CapacitacionesPrincipales','Exp_Laboral' ,'RecomendadoPor']
#
# class Exp_LaboralSerializer (serializers.ModelSerializer):
#     class Meta:
#         model = ExperienciaLaboral
#         fields = ['id', 'Empresa','PuestoOcupado','Fecha_Desde','Fecha_Hasta' ,'Salario']
#
# class EmpleadosSerializer (serializers.ModelSerializer):
#     class Meta:
#         model = Empleados
#         fields = ['id', 'Cedula','Nombre' ,'Fecha_Ingreso','Departamento','Puesto','SalarioMensual','Activo']
