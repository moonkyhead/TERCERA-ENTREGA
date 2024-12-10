from django.shortcuts import render, redirect
from .forms import AutorForm, LibroForm, EditorialForm


# Create your views here.
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
        form = LibroiForm(request.POST)
        if form.is_valid():
            form.save
            return redirect('crear_libro')
        
        else:
            form = LibroiForm()
            return render(request, 'curso/crear_libro.html', {'form': form})
        
        
def crear_editorial(request):
    if request.method == "POST":
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save
            return redirect('crear_editorial.html', {'form': form})











