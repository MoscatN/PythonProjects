Sentencia correcta para iniciar un projecto en CMD:    
python -m django startproject (project)

Se debe crear un Superuser para acceder al apartado de admin 
Este user se creara via el CMD con  python manage.py createsuperuser, aqui 
se ingresa su nombre, correo(no es obligatorio) y password.

     python manage.py shell
Es util para manejar la data ingresada en la app, es posible utilizar un for-each
para acceder a los datos de manera limpia y ordenada. 

OJO: **Tener en cuenta la Identacion tipica de python.**

1. Solucionado Bug de la Datatable, el tbody estaba dentro del for 

Duda: 
Crear a RH usuarios limitados, o hacerlo automaticamente? 

TODO: 
1. Modernizar la view de candidatos. 
2. Testear todas las funciones de cada model. 