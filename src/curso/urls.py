from django.urls import path

from .views import index, about 

from .import views


app_name = "curso"

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("autor/", views.crear_autor, name="crear_autor"),
    path("libros/", views.LibroListView.as_view(), name="libros"),
    path("libros/"<int:pk>/, views.LibroDetailView.as_view(), name="libro_detalle"),
    path("libros/"<int:pk>/update/, views.LibroUpdateView.as_view(), name="libro_update"),
    path("libros/"<int:pk>/delete/, views.LibroDeleteView.as_view(), name="libro_delete"),
]

