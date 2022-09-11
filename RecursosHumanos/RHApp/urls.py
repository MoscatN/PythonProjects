from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('idiomas/', views.idiomas),
    path('capacitaciones/', views.capacitaciones),
    path('competencia/', views.competencia),
    path('puesto/', views.puesto),
    path('explaboral/', views.experienciaLaboral),
    path('empleados/', views.empleados),
    path('candidatos/', views.candidatos),

    path('create_idioma/', views.createIdioma, name="create_idioma")
]