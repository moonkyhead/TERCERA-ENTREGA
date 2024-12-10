from django.shortcuts import render, redirect
from .forms import AutorForm, LibroForm, EditorialForm
from .models import Autor, Libro, Editorial

def index(request):
    return render(request, 'curso/index.html')

def about(request):
    return render(request, 'curso/about.html')



def Autor_list(request):
    autores = Autor.objects.all()  
    context = {'object_list': autores}  
    return render(request, 'Autor/Autor_list.html', context)


def Libro_list(request):
    libros = Libro.objects.all()  
    context = {'object_list': libros}  
    return render(request, 'Libro/Libro_list.html', context)


def Editorial_list(request):
    editoriales = Editorial.objects.all()  
    context = {'object_list': editoriales} 
    return render(request, 'Editorial/Editorial_list.html', context)






