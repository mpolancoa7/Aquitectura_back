from django.db import models

class Productos(models.Model):
    codigo=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    precio=models.DecimalField(max_digits=7,decimal_places=2)
    precio_descuento=models.DecimalField(max_digits=7,decimal_places=2,blank=True,null=True)
    descripcion=models.TextField()
    proveedor=models.CharField(max_length=100)
    beneficios=models.TextField()
    stock=models.IntegerField()
    foto=models.CharField(max_length=200)

    #para personalizar vista de administrador
    def __str__(self):
        return self.nombre