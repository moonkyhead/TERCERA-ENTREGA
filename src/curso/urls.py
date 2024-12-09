from django.urls import path

from .views import index

app_name = "curso"

urlpatterns = [
path("", index, name="index"),
path("", about/, about, name="about"),
]