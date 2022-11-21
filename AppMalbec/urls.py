from django.urls import path
from AppMalbec.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name= "Inicio"),
    path("usuarios/", UsuarioLista.as_view(), name="Usuarios"),
    path("usuarios/nuevo/", UsuarioCrear.as_view(), name= "UsuarioNuevo"),
    path("bazar/",BazarLista.as_view(), name="Bazar"),
    path("bazar/agregar/", BazarCrear.as_view(), name="AgregarBazar"),
    path("variedades/", VariedadesLista.as_view(), name="Variedades"),
    path("variedades/agregar/", VariedadAgregar.as_view(), name ="AgregarVariedad"),
    path("usuarios/<int:pk>/", UsuarioDetalle.as_view(), name ="DetalleUsuario"),
    path("bazar/<int:pk>/", BazarDetalle.as_view(), name= "BazarDetalles"),
    path("variedades/<int:pk>/", VariedadDetalle.as_view(), name= "DetalleVariedad"),
    path("usuarios/editar/<int:pk>/", UsuarioEditar.as_view(), name ="EditarUsuario"),
    path("bazar/editar/<int:pk>/", BazarEditar.as_view(), name= "EditarBazar"),
    path("variedades/editar/<int:pk>/", VariedadEditar.as_view(), name= "EditarVariedad"),
    path("usuarios/borrar/<int:pk>/", UsuarioBorrar.as_view(), name ="BorrarUsuario"),
    path("bazar/borrar/<int:pk>/", BazarBorrar.as_view(), name= "BorrarBazar"),
    path("variedades/borrar/<int:pk>/", VariedadBorrar.as_view(), name= "VariedadBorrar"),
    path("login/", inicio_sesion, name= "Login"),
    path("registro/", registro, name= "Registarse"), 
    path("sobre_mi/", SobreMi, name= "SobreMi" ),
    path("logout/", LogoutView.as_view(template_name="AppMalbec/logout.html"), name="Logout"),
    path("editarPerfil/", editarUsuario, name= "EditarPerfil"),
    path("nuevoAvatar/", agregarAvatar, name= "Avatar"),
]
