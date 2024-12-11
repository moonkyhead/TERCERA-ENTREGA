from django.shortcuts import redirect, render
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

def Autor_create(request):
    if request.method== 'GET':
        form = AutorForm()
    if request.method== 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('curso:Autor_list')
    return render(request, 'Autor/Autor_form.html', {'form':form})


def Libro_list(request):
    libros = Libro.objects.all()  
    context = {'object_list': libros}  
    return render(request, 'Libro/Libro_list.html', context)

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
    return render(request, 'Editorial/Editorial_list.html', context)

def Editorial_create(request):
    if request.method== 'GET':
        form = EditorialForm()
    if request.method== 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('curso:Editorial_list')
    return render(request, 'curso/Editorial_form.html', {'form':form})




