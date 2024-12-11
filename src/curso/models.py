from django.db import models
# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    nacionalidad = models.CharField(max_length=200)
    autor_id = models.CharField
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.nacionalidad})"

    
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    artista = models.CharField(max_length=100) 

    def __str__(self):
        return f"{self.titulo} ({self.fecha_publicacion})"


class Editorial(models.Model):
    nombre = models.CharField(max_length=200)
    escritor = models.CharField(max_length=100, null=True, blank=True)
    


    def __str__(self):
        return f"{self.nombre}"





