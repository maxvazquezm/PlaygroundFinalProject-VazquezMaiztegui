"""
URL configuration for ProycetoFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import (
    cursos_view, 
    inicio_view, 
    profesor_view, 
    estudiante_view,
    cursos_crud_read_view,
    profesores_crud_read_view, 
    estudiantes_crud_read_view,
    profesores_crud_delete_view,
    profesores_crud_update_view,
    # CBV
    CursoCreateView,
    CursoDetail,
    CursoDeleteView,
    CursoListView,
    CursoUpdateView,
    ProfesorCreateView,
    ProfesorDetail,
    ProfesorDeleteView,
    ProfesorListView,
    ProfesorUpdateView,
    EstudianteCreateView,
    EstudianteDetail,
    EstudianteDeleteView,
    EstudianteListView,
    EstudianteUpdateView,
    # Login
    login_view,
    editar_usuario_view,
    registro_view,
    CambiarContrasenia,
    about_us_view
    )

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('inicio/', inicio_view),
    path('cursos/', cursos_view),
    path("profesores/", profesor_view),
    path("estudiantes/", estudiante_view),
    path("cursos-lista/", cursos_crud_read_view),
    path("profesores-lista/", profesores_crud_read_view),
    path("estudiantes-lista/", estudiantes_crud_read_view),
    path("profesores-eliminar/<profesor_email>/", profesores_crud_delete_view),
    path("profesores-editar/<profesor_email>/", profesores_crud_update_view),

    ### CBV

    path("curso/list", CursoListView.as_view(), name="curso-list"),
    path("curso/new", CursoCreateView.as_view(), name="curso-create"),
    path("curso/<pk>", CursoDetail.as_view(), name="curso-detail"),
    path("curso/<pk>/update", CursoUpdateView.as_view(), name="curso-update"),
    path("curso/<pk>/delete", CursoDeleteView.as_view(), name="curso-delete"),

    path("profesor/list", ProfesorListView.as_view(), name="profesor-list"),
    path("profesor/new", ProfesorCreateView.as_view(), name="profesor-create"),
    path("profesor/<pk>", ProfesorDetail.as_view(), name="profesor-detail"),
    path("profesor/<pk>/update", ProfesorUpdateView.as_view(), name="profesor-update"),
    path("profesor/<pk>/delete", ProfesorDeleteView.as_view(), name="profesor-delete"),

    path("estudiante/list", EstudianteListView.as_view(), name="estudiante-list"),
    path("estudiante/new", EstudianteCreateView.as_view(), name="estudiante-create"),
    path("estudiante/<pk>", EstudianteDetail.as_view(), name="estudiante-detail"),
    path("estudiante/<pk>/update", EstudianteUpdateView.as_view(), name="estudiante-update"),
    path("estudiante/<pk>/delete", EstudianteDeleteView.as_view(), name="estudiante-delete"),

    ### Login / Logout
    path("registro", registro_view, name="registro"),
    path("login", login_view, name="login"),

    path("logout", LogoutView.as_view(template_name="AppCoder/logout.html"), name="logout"),

    # Edicion de usuario
    path("editar-usuario", editar_usuario_view, name="editar-usuario"),
    path("cambiar-contrasenia", CambiarContrasenia.as_view(), name="cambiar-contrasenia"),

    path("about_us/", about_us_view),

]