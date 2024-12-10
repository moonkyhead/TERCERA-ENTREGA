from django.contrib import admin

# Register your models here.

from .models import Autor, Libro, Editorial


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'nacionalidad', 'descripcion')
    search_fields = ('nombre', 'apellido')


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion', 'autor')
    search_fields = ('titulo', 'autor')
    
    
@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre','libros')
    search_fields = ('nombre','libros')