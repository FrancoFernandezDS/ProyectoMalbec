from ast import List
from django.shortcuts import render
from AppMalbec.models import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


def inicio(request):
    return render(request, "AppMalbec/inicio.html")

def usuario(request):
    
    return render(request, "AppMalbec/usuario.html")

def bazar(request):
    return render(request, "AppMalbec/bazar.html")

def variedades(request):
    return render(request, "AppMalbec/variedad.html")  


# Create your views here.

class UsuarioLista(ListView):
    model = Usuario
    template_name = "AppMalbec/usuario.html"

class UsuarioCrear(CreateView):
    model = Usuario
    success_url = "/AppMalbec/usuarios/"
    fields = ["nombre", "apellido", "email"]

class UsuarioDetalle(DetailView):
    model= Usuario

class UsuarioEditar(UpdateView):
    model= Usuario
    success_url = "/AppMalbec/usuarios/"
    fields = ["nombre", "apellido", "email"]

class UsuarioBorrar(DeleteView):
    model= Usuario
    success_url = "/AppMalbec/usuarios/"

class BazarLista(ListView):
    model = Bazar
    template_name = "AppMalbec/bazar.html"
    
class BazarCrear(CreateView):
    model= Bazar
    success_url = "/AppMalbec/bazar/"
    fields = ["tipo_de_producto", "precio"]

class BazarDetalle(DetailView):
    model= Bazar

class BazarEditar(UpdateView):
    model= Bazar
    success_url = "/AppMalbec/bazar/"
    fields = ["tipo_de_producto", "precio"]

class BazarBorrar(DeleteView):
    model= Bazar
    success_url = "/AppMalbec/bazar/"

class VariedadesLista(ListView):
    model = Variedad
    template_name = "AppMalbec/variedad.html"

class VariedadAgregar(CreateView):
    model = Variedad
    success_url = "/AppMalbec/variedades/"
    fields = ["categoria", "marca", "precio", "familia"]

class VariedadDetalle(DetailView):
    model= Variedad

class VariedadEditar(UpdateView):
    model = Variedad
    success_url = "/AppMalbec/variedades/"
    fields = ["categoria", "marca", "precio", "familia"]

class VariedadBorrar(DeleteView):
    model = Variedad
    success_url = "/AppMalbec/variedades/"

