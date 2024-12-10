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
    list_display = ('nombre', 'mostrar_libros')  
    search_fields = ('nombre',)

    def mostrar_libros(self, obj):
        return ", ".join([libro.titulo for libro in obj.libros.all()])
    mostrar_libros.short_description = 'Libros'  