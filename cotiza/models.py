from django.db import models

class Clientes(models.Model):
    nombreRepresentante = models.CharField(max_length=200, blank=True)
    nombreOrganizacion = models.CharField(max_length=200, blank=True)


    run=models.CharField(max_length=9, blank=True)
    ciudad= models.CharField(max_length=200, blank=True)

    celular=models.IntegerField(max_length=9, blank=True)
    telefono=models.IntegerField(max_length=9, blank=True)

    
    direccion = models.CharField(max_length=200, blank=True)
    email= models.EmailField()
    def __str__(self):                     
        return '%s' % (self.nombre)

class Trabajadores(models.Model):
    nombre = models.CharField(max_length=100, blank=True)
    sueldoBase = models.DecimalField(max_digits=8, decimal_places=1)
    gratificaciones = models.DecimalField(max_digits=8, decimal_places=1)
    sueldoImponible = models.DecimalField(max_digits=8, decimal_places=1)
    bonos = models.DecimalField(max_digits=8, decimal_places=1)
    Total_haberes = models.DecimalField(max_digits=8, decimal_places=1)
    SIS = models.DecimalField(max_digits=8, decimal_places=1)
    ACHS = models.DecimalField(max_digits=8, decimal_places=1)
    AFC = models.DecimalField(max_digits=8, decimal_places=1)
    sueldos = models.DecimalField(max_digits=8, decimal_places=1)
    sueldo_liquido= models.DecimalField(max_digits=8, decimal_places=1)
    horas_trabajadas = models.DecimalField(max_digits=8, decimal_places=1)
    costo_hora = models.DecimalField(max_digits=8, decimal_places=1)
    costo_dia = models.DecimalField(max_digits=8, decimal_places=1)






    def __str__(self):                     
        return '%s' % (self.trabajador)