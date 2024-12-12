"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from curso.views import *
from curso import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('curso.urls')),
    path("", index, name="index"),  
    path("about/", about, name="about"),
    path("Autor/", Autor_list, name="Autor_list"), 
    path("Libro/", Libro_list, name="Libro_list"),  
    path("Editorial/", Editorial_list, name="Editorial_list"), 
    path("saludar/", views.saludar),
    path("saludar-con-etiqueta/", views.saludar_con_etiqueta),
    path("saludar/<str:nombre>/<str:apellido>", views.saludar_con_parametros),
    path("final/", views.index2),
]


 