from django.urls import path
from .views import index, about, Autor_list, Libro_list, Editorial_list
from django.contrib import admin

app_name = "curso"

from django.urls import path
from .views import index, about, Autor_list, Libro_list, Editorial_list
from django.contrib import admin

app_name = "curso"

urlpatterns = [
    path('admin/', admin.site.urls),  
    path("", index, name="index"),  
    path("about/", about, name="about"),
    path("Autor/", Autor_list, name="Autor_list"), 
    path("Libro/", Libro_list, name="Libro_list"),  
    path("Editorial/", Editorial_list, name="Editorial_list"),  
]


