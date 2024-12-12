from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import AutorForm, LibroForm, EditorialForm
from .models import Autor, Libro, Editorial

def saludar(request):
    return HttpResponse('Lo de Leandrito 2- Proyecto Final')

def saludar_con_etiqueta(request):
    return HttpResponse('<h1>Curso Python Clase 60025</h1>')

def saludar_con_parametros(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f'{apellido}, {nombre}')

def index2(request):
    return render(request, 'curso/index2.html')

def index2(request):
    context= {'año': 2024}
    return render(request, 'curso/index2.html', context)

def index(request):
    return render(request, 'curso/index.html')

def about(request):
    return render(request, 'curso/about.html')



def Autor_list(request):
    autores = Autor.objects.all()  
    context = {'object_list': autores}  
    return render(request, 'curso/Autor_list.html', context)

def Autor_create(request):
    if request.method== 'GET':
        form = AutorForm()
    if request.method== 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('curso:Autor_list')
    return render(request, 'curso/Autor_form.html', {'form':form})


def Libro_list(request):
    libros = Libro.objects.all()  
    context = {'object_list': libros}  
    return render(request, 'curso/Libro_list.html', context)

def Libro_create(request):
    if request.method== 'GET':
        form = LibroForm()
    if request.method== 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('curso:Libro_list')
    return render(request, 'curso/Libro_form.html', {'form':form})


def Editorial_list(request):
    editoriales = Editorial.objects.all()  
    context = {'object_list': editoriales} 
    return render(request, 'curso/Editorial_list.html', context)

def Editorial_create(request):
    if request.method== 'GET':
        form = EditorialForm()
    if request.method== 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('curso:Editorial_list')
    return render(request, 'curso/Editorial_form.html', {'form':form})




