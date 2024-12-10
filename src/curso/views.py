from django.shortcuts import render, redirect
from .forms import AutorForm, LibroForm, EditorialForm
from .models import Autor, Libro, Editorial


def index(request):
    return render(request, 'curso/index.html')


def about(request):
    return render(request, 'curso/about.html')


def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AutorForm()
    return render(request, 'curso/crear_autor.html', {'form': form})


def crear_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)  
        if form.is_valid():
            form.save()  
            return redirect('crear_libro')  
    else:
        form = LibroForm()  
    return render(request, 'curso/crear_libro.html', {'form': form})


def crear_editorial(request):
    if request.method == "POST":
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('crear_editorial')  
    else:
        form = EditorialForm()
    return render(request, 'curso/crear_editorial.html', {'form': form})


def Autor_list(request):
    autores = Autor.objects.all()  
    return render(request, 'Autor/Autor_list.html', {'autores': autores})


def Libro_list(request):
    libros = Libro.objects.all()  
    return render(request, 'Libro/Libro_list.html', {'libros': libros})


def Editorial_list(request):
    editoriales = Editorial.objects.all()  
    return render(request, 'Editorial/Editorial_list.html', {'editoriales': editoriales})






