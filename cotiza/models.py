from django.db import models

class Clientes(models.Model):
    nombreRepresentante = models.CharField(max_length=200, blank=True)
    nombreOrganizacion = models.CharField(max_length=200, blank=True)


    run=models.CharField(max_length=9,blank=True)
    ciudad= models.CharField(max_length=200,blank=True)

    celular=models.IntegerField(blank=True)
    telefono=models.IntegerField(blank=True)

    
    direccion = models.CharField(max_length=200, blank=True)
    email= models.EmailField()
    def __str__(self):                     
        return '%s' % (self.nombreRepresentante)

class Trabajadores(models.Model):
    nombre = models.CharField(max_length=100, blank=True)
    sueldoBase = models.DecimalField(max_digits=9, decimal_places=1)
    gratificaciones = models.DecimalField(max_digits=9, decimal_places=1)
    sueldoImponible = models.DecimalField(max_digits=9, decimal_places=1)
    bonos = models.DecimalField(max_digits=9, decimal_places=1)
    Total_haberes = models.DecimalField(max_digits=9, decimal_places=1)
    SIS = models.DecimalField(max_digits=9, decimal_places=1)
    ACHS = models.DecimalField(max_digits=9, decimal_places=1)
    AFC = models.DecimalField(max_digits=9, decimal_places=1)
    sueldos = models.DecimalField(max_digits=9, decimal_places=1)
    sueldo_liquido= models.DecimalField(max_digits=9, decimal_places=1)
    horas_trabajadas = models.DecimalField(max_digits=9, decimal_places=1)
    costo_hora = models.DecimalField(max_digits=9, decimal_places=1)
    costo_dia = models.DecimalField(max_digits=9, decimal_places=1)

    def __str__(self):                     
        return '%s' % (self.nombre)

class Asesorias(models.Model):
    prevencionista = models.DecimalField(max_digits=9, decimal_places=1)
    sanitizacion = models.DecimalField(max_digits=9, decimal_places=1)
    contabilidad = models.DecimalField(max_digits=9, decimal_places=1)

    mes=models.CharField(max_length=50)
    total=models.DecimalField(max_digits=9, decimal_places=1)
    def __str__(self):                     
        return '%s' % (self.tipo_asesoria)


class GastosAdministrativos(models.Model):
    gastos_comunes= models.DecimalField(max_digits=9, decimal_places=1)
    insumos_aseo= models.DecimalField(max_digits=9, decimal_places=1)
    insumos_oficina= models.DecimalField(max_digits=9, decimal_places=1)
    mantencion_banco= models.DecimalField(max_digits=9, decimal_places=1)
    TI= models.DecimalField(max_digits=9, decimal_places=1)
    arriendo= models.DecimalField(max_digits=9, decimal_places=1)
    patentes= models.DecimalField(max_digits=9, decimal_places=1)
    encomiendas= models.DecimalField(max_digits=9, decimal_places=1)
    ropa_trabajadores= models.DecimalField(max_digits=9, decimal_places=1)
    permisos_circulacion= models.DecimalField(max_digits=9, decimal_places=1)
    generales= models.DecimalField(max_digits=9, decimal_places=1)
    mes=models.CharField(max_length=50)
    total=models.DecimalField(max_digits=9, decimal_places=1)
    def __str__(self):                     
        return '%s' % (self.mes)



class GastosProduccion(models.Model):
    electricidad= models.DecimalField(max_digits=9, decimal_places=1)
    gas_grua= models.DecimalField(max_digits=9, decimal_places=1)
    petroleo= models.DecimalField(max_digits=9, decimal_places=1)
    cordel= models.DecimalField(max_digits=9, decimal_places=1)
    insumos_epp= models.DecimalField(max_digits=9, decimal_places=1)
    mantencion_maquinaria= models.DecimalField(max_digits=9, decimal_places=1)
    insumos_planta= models.DecimalField(max_digits=9, decimal_places=1)
    mes=models.CharField(max_length=50)
    total=models.DecimalField(max_digits=9, decimal_places=1)
    def __str__(self):                     
        return '%s' % (self.mes)

class GastosTotales(models.Model):
    mes=models.CharField(max_length=50)
    sueldos= models.DecimalField(max_digits=9, decimal_places=1)
    total_asesorias= models.DecimalField(max_digits=9, decimal_places=1)
    total_administrativos= models.DecimalField(max_digits=9, decimal_places=1)
    total_produccion= models.DecimalField(max_digits=9, decimal_places=1)
    costo_operativo_dia=models.DecimalField(max_digits=9, decimal_places=1)
    costo_operativo_hora=models.DecimalField(max_digits=9, decimal_places=1)
    costo_operativo_mes=models.DecimalField(max_digits=9, decimal_places=1)
    def __str__(self):                      
        return '%s' % (self.mes)

class Petroleo(models.Model):
    valor_actual= models.DecimalField(max_digits=9, decimal_places=1)

class todo(models.Model):
    #Cliente
    nombre_cliente=models.CharField(max_length=100)
    run=models.CharField(max_length=9,blank=True)
    fecha=models.CharField(max_length=30,blank=True)
    #Conductor
    vehiculo = models.CharField(max_length=3)
    conductor = models.CharField(max_length=100)
    horas_conductor = models.DecimalField(max_digits=8, decimal_places=1)
    kms = models.DecimalField(max_digits=8, decimal_places=1)

    #Ayudantes
    cant_ayudantes=models.IntegerField()

    nombre_asistente1 = models.CharField(max_length=100)
    horas_asistente1= models.DecimalField(max_digits=8, decimal_places=1)

    nombre_asistente2 = models.CharField(max_length=100)
    horas_asistente2= models.DecimalField(max_digits=8, decimal_places=1)

    #Colacion
    valor_colaciones= models.DecimalField(max_digits=8, decimal_places=1)

    #Lugares
    lugar_origen=models.CharField(max_length=150)
    lugar_destino=models.CharField(max_length=150)
    lugar_servicio=models.CharField(max_length=150)

    #Peajes
    suma_peajes=models.DecimalField(max_digits=9, decimal_places=1)

    #Formula
    costo_total= models.DecimalField(max_digits=9, decimal_places=1)
    utilidad= models.DecimalField(max_digits=9, decimal_places=1)
    tarifa= models.DecimalField(max_digits=8, decimal_places=1)
    m3= models.DecimalField(max_digits=8, decimal_places=1)

    





    