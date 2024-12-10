from django.contrib import admin

# Register your models here.

from .models import Autor, Libro, Editorial

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'nacionalidad', 'descripcion')
    search_fields = ('nombre', 'apellido')

    search_fields = ('nombre', 'apellido')
    
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor')
    search_fields = ('titulo', 'autor__nombre', 'autor__apellido', 'editorial__nombre')
    
@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)









