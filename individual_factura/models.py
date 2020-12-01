from django.db import models

# Create your models here.


class Factura(models.Model):

    numero_factura = models.AutoField(primary_key=True)
    anio = models.IntegerField()
    fecha_emision = models.DateField(auto_now_add=True)
    cliente_nombre = models.CharField(max_length=30)
    cliente_direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.cliente_nombre


class LineaDeFactura(models.Model):
    
    factura = models.ForeignKey("Factura", on_delete=models.PROTECT)
    nombre_producto = models.CharField(max_length=30)
    precio_unitario = models.IntegerField()
    unidades = models.IntegerField()

    def __str__(self):
        return self.nombre_producto

    def total(self):
        total = self.precio_unitario * self.unidades
        return total




