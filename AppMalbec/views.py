import re
from tkinter.tix import Form
from django.shortcuts import render
from AppMalbec.models import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from AppMalbec.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, "AppMalbec/inicio.html")

def usuario(request):
    
    return render(request, "AppMalbec/usuario.html")

def bazar(request):
    return render(request, "AppMalbec/bazar.html")

def variedades(request):
    return render(request, "AppMalbec/variedad.html")  

def SobreMi(request):
    return render(request, "AppMalbec/SobreMi.html")

def inicio_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username= usuario, password= contra)

            if user:
                login(request, user)
                return render(request, "AppMalbec/inicio.html", { "mensaje": f"Bienvenido {user}"})

        else:
            return render(request, "AppMalbec/inicio.html", {"mensaje": "Datos incorrectos."})

    else: 
        form = AuthenticationForm() 
    return render(request, "AppMalbec/login.html", {"formulario": form})

def registro(request):
    if request.method == "POST":
        form = UsuarioRegistro(request.POST)

        if form.is_valid():
            username= form.cleaned_data["username"]
            form.save()
            return render(request, "AppMalbec/inicio.html", {"mensaje": "Usuario creado."})
    else:
        form = UsuarioRegistro()  
    return render(request, "AppMalbec/registro.html", {"formulario":form})   


@login_required
def editarUsuario(request):

    usuario = request.user

    if request.method == "POST":
        form = FormEditar(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info ["last_name"]

            usuario.save()

            return render(request, "AppMalbec/inicio.html")
    else:
        form = FormEditar(initial={
            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
        })
    return render(request, "AppMalbec/editarPerfil.html", {"formulario":form, "usuario":usuario})



# Create your views here.

class UsuarioLista(LoginRequiredMixin,ListView):
    model = Usuario
    template_name = "AppMalbec/usuario.html"

class UsuarioCrear(LoginRequiredMixin,CreateView):
    model = Usuario
    success_url = "/AppMalbec/usuarios/"
    fields = ["nombre", "apellido", "email"]

class UsuarioDetalle(LoginRequiredMixin,DetailView):
    model= Usuario

class UsuarioEditar(LoginRequiredMixin,UpdateView):
    model= Usuario
    success_url = "/AppMalbec/usuarios/"
    fields = ["nombre", "apellido", "email"]

class UsuarioBorrar(LoginRequiredMixin,DeleteView):
    model= Usuario
    success_url = "/AppMalbec/usuarios/"

class BazarLista(LoginRequiredMixin,ListView):
    model = Bazar
    template_name = "AppMalbec/bazar.html"
    
class BazarCrear(LoginRequiredMixin,CreateView):
    model= Bazar
    success_url = "/AppMalbec/bazar/"
    fields = ["tipo_de_producto", "precio"]

class BazarDetalle(LoginRequiredMixin,DetailView):
    model= Bazar

class BazarEditar(LoginRequiredMixin,UpdateView):
    model= Bazar
    success_url = "/AppMalbec/bazar/"
    fields = ["tipo_de_producto", "precio"]

class BazarBorrar(LoginRequiredMixin,DeleteView):
    model= Bazar
    success_url = "/AppMalbec/bazar/"

class VariedadesLista(LoginRequiredMixin,ListView):
    model = Variedad
    template_name = "AppMalbec/variedad.html"

class VariedadAgregar(LoginRequiredMixin,CreateView):
    model = Variedad
    success_url = "/AppMalbec/variedades/"
    fields = ["categoria", "marca", "precio", "familia"]

class VariedadDetalle(LoginRequiredMixin,DetailView):
    model= Variedad

class VariedadEditar(LoginRequiredMixin,UpdateView):
    model = Variedad
    success_url = "/AppMalbec/variedades/"
    fields = ["categoria", "marca", "precio", "familia"]

class VariedadBorrar(LoginRequiredMixin,DeleteView):
    model = Variedad
    success_url = "/AppMalbec/variedades/"

