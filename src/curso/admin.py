from django.contrib import admin

# Register your models here.

from .models import Autor, Libro, Editorial


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'nacionalidad', 'descripcion')
    search_fields = ('nombre', 'apellido')












