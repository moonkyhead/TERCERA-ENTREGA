from django.urls import path

from .views import index, about  # Asegúrate de importar la vista `about`

app_name = "curso"

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),  # Ruta corregida para la página "about"
]