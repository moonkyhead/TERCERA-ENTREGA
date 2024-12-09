from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    nacionalidad = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.nacionalidad} {self.descripcion}"

    
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.titulo} {self.fecha_publicacion} {self.autor_id}"
    
class Editorial(models.Model):
    nombre = models.CharField(max_length=200)
    libros = models.ManyToManyField(Libro)
    
    def __str__(self):
        return f"{self.nombre} {self.libros}"














