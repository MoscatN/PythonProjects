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

    path('create_idioma/', views.createIdioma, name="create_idioma"),
    path('update_idioma/<str:pk>/', views.updateIdioma, name="update_idioma"),
    path('delete_idioma/<str:pk>/', views.deleteIdioma, name="delete_idioma"),

    path('create_capacitaciones/', views.createCapacitaciones, name="create_capacitaciones"),
    path('update_capacitaciones/<str:pk>/', views.updateCapacitaciones, name="update_capacitaciones"),
    path('delete_capacitaciones/<str:pk>/', views.deleteCapacitaciones, name="delete_capacitaciones"),
]