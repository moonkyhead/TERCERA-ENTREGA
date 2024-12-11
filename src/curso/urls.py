from django.urls import path
from .views import index, about, Autor_list, Libro_list, Editorial_list


app_name = "curso"

from django.urls import path
from .views import index, about, Autor_list, Libro_list, Editorial_list, Autor_create, Libro_create, Editorial_create


app_name = "curso"

urlpatterns = [  
    path("", index, name="index"),  
    path("about/", about, name="about"),
    path("Autor/list/", Autor_list, name="Autor_list"), 
    path("Autor/create/", Autor_create, name="Autor_create"), 
    path("Libro/list/", Libro_list, name="Libro_list"),  
    path("Libro/create/", Libro_create, name="Libro_create"), 
    path("Editorial/list/", Editorial_list, name="Editorial_list"),  
    path("Editorial/create/", Editorial_create, name="Editorial_create"), 
]


