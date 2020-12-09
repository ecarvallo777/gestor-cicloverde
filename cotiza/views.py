from django.shortcuts import render
from cotiza.models import *
# Create your views here.

def inicio(request):
    all_clients = Clientes.objects.all()

    return render(request, 'index.html', {'clientes':all_clients})


def trabajadores(request):

    all_trabajadores = Trabajadores.objects.all()
    return render(request, 'trabajadores.html',{ 'trabajadores':all_trabajadores} )

def clientes(request):
    all_clients = Clientes.objects.all()
    return render(request, 'clientes.html',{ 'clientes':all_clients} )

def agregarCliente(request):
    organizacion = request.GET["nombreOrganizacion"]
    representante = request.GET["nombreRepresentante"]
    run = request.GET["run"]
    ciudad = request.GET["ciudad"]
    celular= request.GET["celular"]
    telefono = request.GET["telefono"]
    direccion = request.GET["direccion"]
    email = request.GET["email"]

    p = Clientes(nombreOrganizacion=organizacion,
                nombreRepresentante=representante,
                run=run,
                ciudad=ciudad,
                celular=celular,
                telefono=telefono,
                direccion=direccion,
                email=email

    ).save()

    return render(request, 'index.html')

def actualizarClientes(request):

    idd=request.GET["id"]
    upClient= Clientes.objects.get(id=idd)
    upClient.nombreRepresentante=request.GET["nombreRepresentante"]
    upClient.nombreOrganizacion=request.GET["nombreOrganizacion"]
    upClient.run=request.GET["run"]
    upClient.ciudad=request.GET["ciudad"]
    upClient.celular=request.GET["celular"]
    upClient.telefono=request.GET["telefono"]
    upClient.email=request.GET["email"]
    upClient.direccion=request.GET["direccion"]
    upClient.save()

    return render(request, 'index.html')

def actualizarTrabajadores(request):

    idd=request.GET["id"]
    upTrabajador= Trabajadores.objects.get(id=idd)

    upTrabajador.nombre= request.GET["nombre"]
    upTrabajador.SIS= request.GET["sis"]
    upTrabajador.sueldoBase=request.GET["sueldo_base"]
    upTrabajador.ACHS=request.GET["achs"]
    upTrabajador.gratificaciones=request.GET["gratificaciones"]
    upTrabajador.AFC=request.GET["afc"]
    upTrabajador.bonos=request.GET["bonos"]
    upTrabajador.horas_trabajadas=request.GET["horas_trabajadas"]
    upTrabajador.save()


    upTrabajador.sueldo_imponible= float(upTrabajador.sueldoBase) + float(upTrabajador.gratificaciones)  
    upTrabajador.total_haberes=float(upTrabajador.sueldo_imponible)+float(upTrabajador.bonos)
    upTrabajador.sueldos=float(upTrabajador.total_haberes)+float(upTrabajador.SIS) +float(upTrabajador.ACHS)+float(upTrabajador.AFC)
    upTrabajador.sueldo_liquido=float(upTrabajador.sueldoBase) + float(upTrabajador.bonos)
    print(upTrabajador.sueldos)

    upTrabajador.costo_hora=float(upTrabajador.sueldos) / float(upTrabajador.horas_trabajadas)
    upTrabajador.costo_dia=float(upTrabajador.costo_hora) *9
    
    upTrabajador.save()

    

    return render(request, 'index.html')

def agregarTrabajador(request):
    nombre= request.GET["nombre"]
    sis = request.GET["sis"]
    sueldo_base = request.GET["sueldo_base"]
    achs=request.GET["achs"]
    gratificaciones=request.GET["gratificaciones"]
    afc=request.GET["afc"]
    bonos=request.GET["bonos"]
    horas_trabajadas=request.GET["horas_trabajadas"]

    sueldo_imponible= int(sueldo_base) + int(gratificaciones)
    total_haberes=sueldo_imponible+int(bonos)
    sueldos=total_haberes+int(sis)+int(achs)+int(afc)
    sueldo_liquido=int(sueldo_base)+int(bonos)
    costo_hora=sueldos/int(horas_trabajadas)
    costo_dia=costo_hora*9

    p = Trabajadores(nombre=nombre,
                     sueldoBase=sueldo_base,
                     gratificaciones=gratificaciones,
                     sueldoImponible=sueldo_imponible,
                     bonos=bonos,
                     Total_haberes=total_haberes,
                     SIS=sis,
                     ACHS=achs,
                     AFC=afc,
                     sueldos=sueldos,
                     sueldo_liquido=sueldo_liquido,
                     horas_trabajadas=horas_trabajadas,
                     costo_hora=costo_hora,
                     costo_dia=costo_dia).save()
    return render(request, 'index.html')

def cotizar(request):
    vehiculo = request.GET["vehiculo"]
    conductor = request.GET["conductor"]
    colacion = request.GET["colacion"]


    return render(request, 'cotizar.html', {'vehiculo':vehiculo, 'conductor':conductor, 'colacion':colacion})

def vermasclientes(request):

    currentid= request.GET['id']

    currentCliente= Clientes.objects.get(id=currentid)


    return render(request, 'vermasclientes.html', {'currentCliente':currentCliente})

def vermastrabajadores(request):

    currentid= request.GET['id']

    currentTrabajador= Trabajadores.objects.get(id=currentid)


    return render(request, 'vermastrabajadores.html', {'currentTrabajador':currentTrabajador})