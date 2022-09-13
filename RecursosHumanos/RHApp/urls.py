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
    # path('export_pdf', views.exportPDF, name="export_pdf"),

    path('create_idioma/', views.createIdioma, name="create_idioma"),
    path('update_idioma/<str:pk>/', views.updateIdioma, name="update_idioma"),
    path('delete_idioma/<str:pk>/', views.deleteIdioma, name="delete_idioma"),

    path('create_capacitaciones/', views.createCapacitaciones, name="create_capacitaciones"),
    path('update_capacitaciones/<str:pk>/', views.updateCapacitaciones, name="update_capacitaciones"),
    path('delete_capacitaciones/<str:pk>/', views.deleteCapacitaciones, name="delete_capacitaciones"),

    path('create_competencia/', views.createCompetencias, name="create_competencia"),
    path('update_competencia/<str:pk>/', views.updateCapacitaciones, name="update_competencia"),
    path('delete_competencia/<str:pk>/', views.deleteCompetencia, name="delete_competencia"),

    path('create_explaboral/', views.createExpLaboral, name="create_explaboral"),
    path('update_explaboral/<str:pk>/', views.updateExpLaboral, name="update_explaboral"),
    path('delete_explaboral/<str:pk>/', views.deleteExpLaboral, name="delete_explaboral"),

    path('create_puesto/', views.createPuesto, name="create_puesto"),
    path('update_puesto/<str:pk>/', views.updatePuesto, name="update_puesto"),
    path('delete_puesto/<str:pk>/', views.deletePuesto, name="delete_puesto"),

    path('create_candidatos/', views.createCandidatos, name="create_candidatos"),
    path('update_candidatos/<str:pk>/', views.updateCandidatos, name="update_candidatos"),
    path('delete_candidatos/<str:pk>/', views.deleteCandidatos, name="delete_candidatos"),

    path('create_empleados/', views.createEmpleados, name="create_empleados"),
    path('update_empleados/<str:pk>/', views.updateEmpleados, name="update_empleados"),
    path('delete_empleados/<str:pk>/', views.deleteEmpleados, name="delete_empleados"),


]