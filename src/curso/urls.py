from django.urls import path

from .views import index, about 

from .import views


app_name = "curso"

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("autor/", views.crear_autor, name="crear_autor"),
    path("libros/", views.crear_libro, name="crear_libro"),
    path("editorial/", views.crear_editorial, name="crear_editorial"),
]

