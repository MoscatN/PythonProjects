from rest_framework import routers
from RHApp.viewsets import IdiomaViewSet, CompetenciaViewSet, CapacitacionesViewSet, PuestoViewSet, CandidatosViewSet, Exp_LaboralViewSet, EmpleadosViewSet

router = routers.SimpleRouter()
router.register(r'idioma', IdiomaViewSet)
router.register(r'competencia', CompetenciaViewSet, basename='competencia')
router.register(r'capacitaciones', CapacitacionesViewSet, basename='capacitaciones')
router.register(r'puesto', PuestoViewSet, basename='puesto')
router.register(r'candidatos', CandidatosViewSet, basename='candidatos')
router.register(r'ExperienciaLaboral', Exp_LaboralViewSet, basename='ExperienciaLaboral')
router.register(r'empleados', EmpleadosViewSet, basename='empleados')


from django.contrib import admin
from django.urls import path, include

from routers import router

urlpatterns = router.urls

