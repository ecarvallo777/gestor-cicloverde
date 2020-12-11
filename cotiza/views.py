from django.shortcuts import render
from cotiza.models import *
# Create your views here.

def inicio(request):
    all_clients = Clientes.objects.all()
    all_trabajadores= Trabajadores.objects.all()

    return render(request, 'index.html', {'clientes':all_clients, 'trabajadores':all_trabajadores})


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
    ###Información básica:

    nombre_organizacion= request.GET["browser"]
    organizacion = Clientes.objects.get(nombreOrganizacion=nombre_organizacion)
    run= organizacion.run
    fecha = request.GET["fecha_requerida"]
    lugar_origen = request.GET["lugar_origen"]
    lugar_destino = request.GET["lugar_destino"]
    lugar_servicio = request.GET["lugar_servicio"]
    #Vehículo a utilizar  #########################################################################
    vehiculo = request.GET["vehiculo"]

    # Costo operativo empresa x hora según vehíchulo ################################################################
    costo_operativo_empresa = GastosTotales.objects.all().order_by("-id")[0]
    costo_operativo = float(costo_operativo_empresa.costo_operativo_hora)

    if (vehiculo =="KIA"):
        costo_operativo = costo_operativo * 1
    if (vehiculo=="NQR"):
        costo_operativo = costo_operativo * 2

    # get kms a recorrer ###########################################################################
    kms=float(request.GET["kms"])

    # get valor actual petroleo 
    petroleo = Petroleo.objects.get(id=1)
    petroleo_valor=float(petroleo.valor_actual)


    #get petroleo a utilizar ######################################################################

    if (vehiculo == "KIA"):
        petroleo_necesario = ( kms / 10 ) * petroleo_valor 
    if (vehiculo == "NQR"):
        petroleo_necesario = ( kms / 5) * petroleo_valor

    ############ Peajes ###########
    #Peaje lateral
    cantidad_lateral=0
    valor_lateral=0
    state0_lateral= request.GET["cantidad_lateral"]
    state1_lateral=request.GET["valor_lateral"]
    if (state0_lateral != ""): 
        cantidad_lateral=float(state0_lateral)

    if (state1_lateral !=""):
        valor_lateral= float(state1_lateral)

    #Peaje troncal
    cantidad_troncal=0
    valor_troncal=0
    state0_troncal = request.GET["cantidad_troncal"]
    state1_troncal = request.GET["valor_troncal"]

    if(state0_troncal != ""):
        cantidad_troncal = float(state0_troncal)
    if (state1_troncal !=""):
        valor_troncal= float(state1_troncal) 
                            
    #Pase diario
    cantidad_diario=0
    valor_diario=0
    state0_diario= request.GET["cantidad_diario"]
    state1_diario=request.GET["valor_diario"]
    if (state0_diario !=""):
        cantidad_diario= float(state0_diario)
    if (state1_diario !=""):
        valor_diario= float(state1_diario)

    # Suma de peajes ##############################################################
    sum_peajes = (cantidad_lateral*valor_lateral)+(cantidad_troncal*valor_troncal)+(cantidad_diario*valor_diario)

    #### Conductor y asistente ####
    ### Chofer
    #id
    id_chofer= request.GET["conductor"]
    #Costo x chofer
    chofer=Trabajadores.objects.get(id=id_chofer)   

    costo_chofer= float(chofer.costo_hora)
    #Nombre chofer
    nombre_chofer = chofer.nombre 

    #horas trabajadas chofer
    horas_chofer = float(request.GET["horas_chofer"])

    # Horas x costo chofer/hora ###################################################
    chofer_horas = costo_chofer * horas_chofer

    ### Asistente 1
    asistentes=0
    #id 
    id_asistente1= request.GET["ayudante1"]
    asistente1_horas=0
    nombre_asistente1 =""
    horas_asistente1=0
    if(id_asistente1 != ""):
        asistentes= asistentes+1
        #Costo x asistente
        asistente1 = Trabajadores.objects.get(id=id_asistente1)
        costo_asistente1 = float(asistente1.costo_hora)

        #Nombre asistente 1
        nombre_asistente1 = asistente1.nombre

        #Horas trabajadas asistente 1
        horas_asistente1 = request.GET["horas_asistente_1"]

        #Horas x costo asistente1/hora #################################################
        if(horas_asistente1 != ""):
            horas_asistente1 = float(horas_asistente1)
            if (horas_asistente1>0):
                        asistente1_horas = costo_asistente1 * horas_asistente1


    #Asistente 2:
    #id
    id_asistente2 = request.GET["ayudante2"]
    asistente2_horas=0
    nombre_asistente2 =""
    horas_asistente2=0
    if(id_asistente2 != ""):
        asistentes=asistentes+1
        #Costo x asistente
        asistente2 = Trabajadores.objects.get(id=id_asistente2)
        costo_asistente2 = float(asistente2.costo_hora)

        #Nombre asistente 2
        nombre_asistente2=asistente2.nombre

        #Horas trabajadas asistente 2:
        horas_asistente2 = float(request.GET["horas_asistente_2"])

        #Horas x costo asistente2/hora #################################################
        if(horas_asistente2 != ""):
            horas_asistente2 = float(horas_asistente2)
            if (horas_asistente2>0):
                        asistente2_horas = costo_asistente2 * horas_asistente2

    ########Colaciones
    colacion = request.GET["colacion"]
    valor_colacion=0
    if (colacion=="si"):
        valor_colacion=5000
        if(id_asistente1 !="" ):
            valor_colacion=valor_colacion+(5000)
            if(id_asistente2 !=""):
                valor_colacion=valor_colacion+5000

    ## CALCULOS!!
    costo_total= costo_operativo + petroleo_necesario + sum_peajes + chofer_horas +  asistente1_horas + asistente2_horas + valor_colacion
    utilidad30= costo_total*0.3
    tarifa = costo_total+utilidad30
    m3 = tarifa/15

    i = todo (nombre_cliente=nombre_organizacion,
                run=run,
                vehiculo=vehiculo,
                conductor=nombre_chofer,
                horas_conductor=horas_chofer,
                cant_ayudantes=asistentes,
                nombre_asistente1=nombre_asistente1,
                horas_asistente1=horas_asistente1,
                nombre_asistente2=nombre_asistente2,
                horas_asistente2=horas_asistente2,
                valor_colaciones=valor_colacion,
                lugar_origen=lugar_origen,
                lugar_destino=lugar_destino,
                lugar_servicio=lugar_servicio,
                suma_peajes=sum_peajes,
                costo_total=costo_total,
                utilidad=utilidad30,
                tarifa=tarifa,
                m3=m3,
                fecha=fecha,

            ).save()

    return render(request, 'index.html')

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
    petroleo = Petroleo.objects.get(id=1)
    return render(request, 'gastos.html', {'all_gastos':all_gastos, 'petroleo':petroleo})

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

def eliminarTrabajador(request):
    currentTrabajador = request.GET['idregistro']
    eliminate = Trabajadores.objects.get(id=currentTrabajador)
    eliminate.delete()

    return render(request, 'index.html')
    
def eliminarCliente(request):
    currentCliente = request.GET['idregistro']
    eliminate = Clientes.objects.get(id=currentCliente)
    eliminate.delete()
    return render(request, 'index.html')

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

    return render(request, 'index.html')

def volverRegistro(request):

    return render(request, 'index.html/')

def modPetroleo(request):


    getPetroleo= request.GET["petroleo"]
    actual = Petroleo.objects.get(id=1)
    actual.valor_actual = getPetroleo
    actual.save()

    return render(request, 'index.html')

def cotizaciones(request):

    all_cotizaciones = todo.objects.all()

    return render(request, 'cotizaciones.html', {'cotizaciones':all_cotizaciones})

def vermascotizaciones(request):
    return render(request, 'vermascotizaciones.html')