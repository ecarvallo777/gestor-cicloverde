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

def verGastos(request):

    all_gastos = GastosTotales.objects.all()
    return render(request, 'gastos.html', {'all_gastos':all_gastos})

def agregarGastos(request):

    currentMes = request.GET['mes']
    if GastosTotales.objects.filter(mes=currentMes).exists():
        return render(request, 'duplicado.html', {'currentMes':currentMes})
    else:
        prevencionistaa= int(request.GET['prevencionista'])
        sanitizacion=int(request.GET['sanitizacion'])
        contabilidad=int(request.GET['contabilidad'])
        totalasesoria =(prevencionistaa + sanitizacion + contabilidad)
        i = Asesorias(
            prevencionista=prevencionistaa, 
            sanitizacion=sanitizacion,
            contabilidad=contabilidad,
            total=totalasesoria,
            mes=currentMes
            )
        i.save()


    
        gastos_comunes = request.GET['gastos_comunes']
        insumos_aseo=request.GET['insumos_aseo']
        insumos_oficina=request.GET['insumos_oficina']
        mantencion_banco=request.GET['mantencion_banco']
        TI=request.GET['TI']
        arriendo=request.GET['arriendo']
        patentes=request.GET['patentes']
        encomiendas=request.GET['encomiendas']
        ropa_trabajadores=request.GET['ropa_trabajadores']
        permisos_circulacion=request.GET['permisos_circulacion']
        generales=request.GET['generales']
        total=float(gastos_comunes) + float(insumos_aseo) + float(insumos_oficina)+ float(mantencion_banco) + float(TI)+ float(arriendo)+ float(patentes) + float(encomiendas) + float(ropa_trabajadores) +float(permisos_circulacion) + float(generales)


        insertAdministrativos = GastosAdministrativos(gastos_comunes=gastos_comunes,
                                                    insumos_aseo=insumos_aseo,
                                                    insumos_oficina=insumos_oficina,
                                                    mantencion_banco=mantencion_banco,
                                                    TI=TI,
                                                    arriendo=arriendo,
                                                    patentes=patentes,
                                                    encomiendas=encomiendas,
                                                    ropa_trabajadores=ropa_trabajadores,
                                                    permisos_circulacion=permisos_circulacion,
                                                    generales=generales,
                                                    total=total,
                                                    mes=currentMes).save()

        electricidad = request.GET['electricidad']
        gas_grua = request.GET['gas_grua']
        petroleo = request.GET['petroleo']
        cordel = request.GET['cordel']
        insumos_epp = request.GET['insumos_epp']
        mantencion_maquinaria = request.GET['mantencion_maquinaria']
        insumos_planta = request.GET['insumos_planta']
        total = float(electricidad) + float(gas_grua) + float(petroleo) + float(cordel) + float(insumos_epp)+float(mantencion_maquinaria)+ float(insumos_planta)


        insertProduccion = GastosProduccion(electricidad=electricidad,
                                            gas_grua=gas_grua,
                                            petroleo=petroleo,
                                            cordel=cordel,
                                            insumos_epp=insumos_epp,
                                            mantencion_maquinaria=mantencion_maquinaria,
                                            insumos_planta=insumos_planta,
                                            total=total,
                                            mes=currentMes).save()


        # Calculo suma de sueldos de trabajadores
        trabajadores = Trabajadores.objects.all()
        sueldos=0
        for trabajador in trabajadores:
            sueldos = sueldos + trabajador.sueldos 
    
        # Calculo de total de asesorías
        currentAsesoria= Asesorias.objects.get(mes=currentMes)

        # Calculo de total de GastosAdministrativos
        currentAdministrativos = GastosAdministrativos.objects.get(mes=currentMes)

        # Calculo de total de GastosProduccion
        currentProduccion = GastosProduccion.objects.get(mes=currentMes)

        # Calculos Costo costo_operativo_mes
        costo_mensual= sueldos + currentAsesoria.total + currentAdministrativos.total + currentProduccion.total

        insertTotales = GastosTotales(mes=currentMes,
                                    sueldos=sueldos,
                                    total_asesorias= currentAsesoria.total,
                                    total_administrativos=currentAdministrativos.total,
                                    total_produccion=currentProduccion.total,
                                    costo_operativo_mes= costo_mensual,
                                    costo_operativo_dia= costo_mensual / 30,
                                    costo_operativo_hora= (costo_mensual/30)/9 ).save()

    

        return render(request, 'index.html')

def vermasgastos(request):
    currentGasto= request.GET['id']
    mesGasto= GastosTotales.objects.get(id=currentGasto)
    return render(request, 'vermasgastos.html', {'mesGasto':mesGasto})


def eliminarRegistro(request):
    currentId= request.GET['idregistro']
    currentMes= request.GET['idmes']
    eliminate = GastosTotales.objects.get(id=currentId)
    eliminate.delete()

    eliminateA= Asesorias.objects.get(mes=currentMes)
    eliminateA.delete()

    eliminateADM= GastosAdministrativos.objects.get(mes=currentMes)
    eliminateADM.delete()

    eliminatePROD= GastosProduccion.objects.get(mes=currentMes)
    eliminatePROD.delete()

    return render(request, 'gastos.html')