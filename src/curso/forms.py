from django import forms
from .models import Autor, Libro, Editorial

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'nacionalidad', 'descripcion']
        
        
class LibroiForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'fecha_publicacion', 'autor', 'editorial', 'descripcion', 'imagen']
        

class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = ['nombre', 'sitioweb', 'descripcion']
        









