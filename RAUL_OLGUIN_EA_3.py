"""
   La productora de eventos “Sanchez Producciones”, necesita desarrollar una aplicación que permita controlar la venta de entradas
 al concierto de “Michael Jackson” que se realizará de forma exclusiva solo para 50 asistentes. 
 El sistema debe permitir las siguientes operaciones, a través de un menú:

1.	Comprar entradas
2.	Mostrar ubicaciones disponibles
3.	Ver listado de asistentes
4.	Mostrar ganancias totales
5.	Salir

Las características de cada operación, se detallan a continuación:

Comprar entradas: El sistema debe solicitar al usuario la cantidad de entradas a comprar. Esta cantidad fluctúa entre 1 y 2.
Una vez ingresada la cantidad validada, el sistema debe desplegar en pantalla las ubicaciones que se encuentran disponibles 
y las vendidas marcadas con una X. Ejemplo:

								     ESCENARIO
				
1	2	3	4	5	6	7	8	9	10
11	12	13	14	15	16	17	18	19	20
21	22	23	24	25	26	27	28	29	30
31	32	33	34	35	36	37	38	39	40
41	42	43	44	45	46	47	48	49	50

			
						 ESCENARIO CON ASIENTOS COMPRADOS
1	2	3	X	5	6	7	8	9	10
11	12	13	14	15	16	17	18	19	20
21	22	23	X	25	26	27	28	29	30
31	X	33	34	35	36	37	38	39	40
41	42	43	44	45	46	X	48	49	50

El usuario debe seleccionar una a una las ubicaciones. Si selecciona una ubicación vendida, se desplegará por pantalla un mensaje que “No está disponible”, teniendo que seleccionar otra.
Los precios de las entradas son los siguientes:

1.	VIP, $100.000. (Asientos del 1 al 20).
2.	Normal $50.000. (Asientos del 21 al 30).
3.	Económico, $10.000. (Asientos del 31 al 50)

Cada asiento debe tener registrado el RUN de la persona que lo ocupará.
 El RUN se debe registrar en formato de número, sin guion, puntos ni dígito verificador (Ejemplo: 12.345.678-9, debe ser 12345678).

Posteriormente, debe mostrar un mensaje que indique que la operación se ha realizado correctamente.

Mostrar ubicaciones disponibles: El sistema debe desplegar el estado actual de la venta de entradas.
 Esto se debe desplegar de la misma forma que se muestra en la imagen de la opción de “Escenario con asientos comprados”.

Ver listado de asistentes: El sistema debe mostrar el listado de asistentes por RUN,
 ordenados de menor a mayor, con la finalidad encontrar fácilmente a una persona asistente.

Mostrar ganancias totales: El sistema debe calcular el total ganado por concepto de entradas y desplegarse la información


OTRAS CONSIDERACIONES:
1.	El sistema debe validar las opciones del menú.
2.	Cada opción del menú debe ejecutarse a través de funciones.
3.	La opción Salir debe mostrar un mensaje de salida del sistema, su nombre, apellido y la fecha actual.
4.	El sistema debe realizar todas las validaciones necesarias requeridas en el ingreso de datos.
5.	Los datos ingresados se almacenan en arreglos. (Seleccione el tipo de arreglo, de acuerdo a su criterio).
6.	Considere listas para alguna de las opciones.
7.	Se debe utilizar Github para la entrega del código fuente


"""

import os
import datetime

# constantes para modificar en caso de necesitar mas asientos o en un orden distinto
largoFila = 5
largoColumnas = 10

# llenando el arreglo con los asientos
# es un arreglo de diccionarios donde la clave es el asiento y el valor el rut de la persona
# como se esta inicializando el rut es 0

# la formula para calcular el asiento es (fila * largo columnas) + la columna + 1 
# ejemplo (0 * 10) + 5 + 1 = asiento 6 (en la columna 5 de la fila 0)

asientos = [{(( fil * largoColumnas) + col + 1):0 for col in range(largoColumnas)} for fil in range(largoFila)]


# Cada valor representa el precio de un asiento de la  fila
# ej cada asiento de la fila 0 cuesta 10 millones  
precios = [100_000,100_000,50_000,10_000,10_000]



#--------------------------------------------------------------------------------------------------
# funcion que muestra los asientos disponibles y ocupados

def mostrar():

    print("\n\t")
    for fila in asientos:
        for asiento, rut in fila.items():
            if rut == 0:
                # si el numero es menor a 10 se muestra con un espacio mas 
                numero_mostrar = f"[ {asiento}  ]" if asiento < 10 else f"[ {asiento} ]"
                
                print(numero_mostrar, end="")
            else:
                print("( X  )", end="")
        print("\t")

#--------------------------------------------------------------------------------------------------
# funcion que permite comprar un asiento
# retorna true cuando la compra se ha hecho y false cuando no
# no se efectua la compra cuando se elige un asiento ocupado

def comprar():

    mostrar()

    try:
        rut = int(input("\n\tingrese rut de Asistente (numerico sin puntos ni guion) >> "))
    except(ValueError, TypeError):
        print(f"\n\n\tINGRESE RUT VALIDO NUMERICO SIN PUNTOS NI GUION")
        compra = 0
        return False

    try:
        compra = int(input("\n\tingrese asiento a comprar >> "))
    except(ValueError, TypeError):
        print(f"\n\n\tINGRESE OPCION VALIDA ENTRE 1 Y {largoFila * largoColumnas} compra no efectuada")
        compra = 0
        return False

    if compra in range(1, (largoFila*largoColumnas)+1):

        # fila donde esta el asiento a comprar        
        fila = compra//largoColumnas

        # si el asiento comprado es borde se corrige 
        if (compra % largoColumnas) == 0:
            fila -= 1
        
        # comprando el asiento
        if asientos[fila][compra] == 0:
            asientos[fila][compra] = int(rut)
            print("\n\tAsiento comprado, la operación se ha realizado correctamente\n")
            return True
        
        else:
            print("\n\tAsiento Ocupado, Compra NO Efectuada\n")
            return False
    else:
        print(f"\n\tAsiento no Valido ingrese opcion entre 1 y {largoFila * largoColumnas} , Compra NO Efectuada\n")
        return False

#--------------------------------------------------------------------------------------------------
# funcion calculo de ganancias totales

def ganancias_totales():
    ganancia = 0
    contador = 0
    fila = 0
    
    for filas in asientos:
        for asiento in filas:
            if(filas[asiento] != 0):
                ganancia += precios[fila]
                contador +=1
        fila += 1 

    print(f"\n\n\tSe han vendido {contador} entradas con una ganancia total de { " {:,}".format(ganancia).replace(",",".") }\n\n")



#--------------------------------------------------------------------------------------------------
# funcion muestra compradores

def asistentes():
       
    auxAsistente = []

    for filas in asientos:
        for asiento in filas:
            if filas[asiento] != 0:
                auxAsistente.append(filas[asiento])
    auxAsistente.sort()
    cont = 0
    print("\n\t El listado de asistentes es: \n\t")
    for persona in auxAsistente:
        print(f" [ {persona} ] ",end="")
        cont += 1
        if cont % largoColumnas == 0:
            print("")


#--------------------------------------------------------------------------------------------------
# menu
while True:
    os.system('cls')

    print("\n\n\t*** MENU PRINCIPAL ***")
    print("\n\tOPCION 1: Comprar entradas")
    print("\tOPCION 2: Mostrar ubicaciones disponibles")
    print("\tOPCION 3: Ver listado de Asistentes")
    print("\tOPCION 4: Mostrar ganancias totales")
    print("\tOPCION 5: Salir")
           
    opcion = int(input("\t>> <<\b\b\b"))

    if opcion == 5:
        os.system("cls")
        print(f"\n\tAdios, Gracias por su preferencia\n\tRAUL OLGUIN ROMO\n\t{datetime.datetime.now()}\n\n")
        break

    elif opcion == 1:
        os.system("cls")

        print("\n\n\t*** MENU COMPRA ENTRADAS ***")
        
        opcionCompra = -1
        while opcionCompra not in (0,1,2):

            try:
                opcionCompra = int(input("\n\tCuantas entradas desea comprar 0,1,2 >> "))# 0 para cuando se arrepientan de comprar
            except(ValueError, TypeError):
                opcionCompra = -1
            except:
                opcionCompra = -1

            if opcionCompra not in (0,1,2):
                print("\n\n\t ingrese una opcion valida 0, 1, 2\n\n")


        if opcionCompra != 0:
            contador = 0 #contador compras
            while contador < opcionCompra:
                compra_hecha = comprar()
                if compra_hecha:
                    contador += 1
                
        input("\n\n\t>>> presione ENTER para continuar <<<")
    elif opcion == 2:
        os.system("cls")

        print("\n\n\t*** MENU MOSTRAR UBICACIONES ***")
        mostrar()
        
        input("\n\n\t>>> presione ENTER para continuar <<<")

    elif opcion == 4:
        os.system("cls")

        print("\n\n\t*** GANANCIAS TOTALES ***")
        ganancias_totales()

        input("\n\n\t>>> presione ENTER para continuar <<<")

    elif opcion == 3:
        os.system("cls")

        print("\n\n\t*** LISTA DE ASISTENTES ***")
        asistentes()

        input("\n\n\t>>> presione ENTER para continuar <<<")
    else:
        print("opcion no valida")
        input("\n\n\t>>> presione ENTER para continuar <<<")