from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):

        return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('No tiene las credenciales para ver esta pagina.')
            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator

def RH_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'Postulante':
            messages.info(request, 'No tiene las credenciales para ver esta pagina.')
            return redirect('/candidatos')

        if group == 'RH':
            return view_func(request, *args, **kwargs)

    return wrapper_function
