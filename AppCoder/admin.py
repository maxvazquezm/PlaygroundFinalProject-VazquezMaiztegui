from django.contrib import admin

# Register your models here.

from .models import Curso, Profesor, Estudiante


@admin.register(Curso,Profesor,Estudiante)
class CursoAdmin(admin.ModelAdmin):
    pass
class ProfesorAdmin(admin.ModelAdmin):
    pass
class EstudianteAdmin(admin.ModelAdmin):
    pass