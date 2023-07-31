from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from vehiculo.models import *
from django.views.generic import TemplateView
from .forms import VehiculoForm, SignInForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import login, authenticate, logout
from tokenize import PseudoExtras
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class IndexPageView(TemplateView, LoginRequiredMixin, PermissionRequiredMixin):
    login_url = '/login/'
    permission_required = 'vehiculo.view_vehiculo' #permiso de vista
    template_name = 'index.html'
    

def login_view(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            usuario = authenticate(usename=username,password=password)
            if usuario is not None:
                login(request,usuario)
                messages.info(request,'Sesión activa')
                return HttpResponseRedirect("/")
            else:
                messages.error(request,'Usuario o Contraseña erronea')
        else:
            messages.error(request,'Usuario o Contraseña erronea')
    
    formulario = AuthenticationForm()
    context = {'login_form': formulario }
    return render(request,'login.html', context)


def add_view(request):
    if request.method == 'POST':
        formulario = VehiculoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/vehiculos/add")
    else:
        formulario = VehiculoForm()
    
    context = {'form': VehiculoForm() }
    return render(request,'add.html', context)

def logout_view(request):
    pass

def signin_view(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            #content_type = ContentType.objects.get_for_model(Vehiculo)
            #visualizar_catalogo = Permission.objects.get(codename='view_vehiculo', content_type=content_type)
            user = form.save()
            #user.user_permissions.add(visualizar_catalogo)
            login(request, user)
            messages.success(request, "Registrado Satisfactoriamente.")
            return HttpResponseRedirect('/')
        messages.error(request, "Registro invalido. Algunos datos sonincorrectos.")
    else:
        form = SignInForm()

    context = {'register_form':form}
    return render(request,'signin.html',context)

#revisar
def lista_view(request):
    datos = Vehiculo.objects.filter().values('id','marca', 'modelo', 'serial_carroceria','serial_motor', 'categoria', 'precio')
    condicion = ""
    for item in datos:
        precio = item['precio']
        if precio > 30000:
            condicion = 'Alto'
        if precio > 10000:
            condicion = 'Medio'
        else:
            condicion = 'Baja'
        item['condicion'] = condicion
    context = {'lista': datos}
    return render(request,'lista.html',context)