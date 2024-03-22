#El presente archivo toma como base la tarea de "Programar el comportamiento de la reina y la nodriza" del punto anterior.

from pprint import pprint
import sys
import random
import os
import matplotlib.pyplot as plt
import numpy as np
from math import trunc

#Variable global
contadorHormigas = []
mesDelAno = random.randint(1,12)
expulsados = []

#Función de la reina
def hormigaReina():

    #huevos = trunc(random.randint(20, 50))         #Se decidió dejar esta cantidad de huevos ya que es una cantidad anual
    huevos = trunc(random.randint(7300, 182500))    #es decir, la cantidad entre 20 y 50 huevos se ultiplicó por 365 
    hormigaNodriza(huevos)                          #(asumiendo que no es un año bisiesto)

    orden = random.randint(0,500)                   #La probabilidad de que la reina ordene atacar o defender la colonia
    if( orden >= 400):
        hormigaSoldado( 'Atacar' )
    else:
        hormigaSoldado( 'Custodiar' )
    return();


#Función de la nodriza
def hormigaNodriza( huevos ):

    cantidadObreras = huevos * 0.8                  # la cantidad de hormigas obreras es del 80% del total
    cantidadSoldado = huevos * 0.15                 # la cantidad de hormigas soldado es del 15% del total
    cantidadNodriza = huevos * 0.04                 # la cantidad de hormigas nodriza es del 4% del total
    cantidadRealeza = huevos * 0.01                 # la cantidad de hormigas de la realeza es del 1% del total
    cantidadSepulturera = random.randint(1,trunc(cantidadObreras*0.01))     # Del total de obreras, sacamos el 1% para asegurarnos de tener como mínimo una sepulturera
    cantidadObreras = cantidadObreras - cantidadSepulturera                 # Descontamos las sepultureras añadidas a la cantidad de obreras

    #A nuestra lista global, se le agregan la cantidad de hormigas según su tipo
    contadorHormigas.append(trunc(cantidadObreras))
    contadorHormigas.append(trunc(cantidadSoldado))
    contadorHormigas.append(trunc(cantidadNodriza))
    contadorHormigas.append(trunc(cantidadRealeza*0.5))
    contadorHormigas.append(trunc(cantidadRealeza*0.5))
    contadorHormigas.append(trunc(cantidadSepulturera))

    #Al usar trunc, se pueden generar pérdidas de la cantidad de "hormigas", por lo que para asegurarnos de que
    #el total de hormigas no se vea alterado, se realiza una condicional en la que de existir una diferencia
    #entre la cantidad de huevos y la cantidad guardada en contadorHormiga, la diferencia de estas se le suma
    #a las hormigas sepultureras, para así matnener el equilibrio de hormigas.
    if(huevos > sum(contadorHormigas)):
        cantidadSepulturera = cantidadSepulturera + (huevos - sum(contadorHormigas))

    hormigaPrincipe()
    hormigaPrincesa()

    print("==================================")
    print("LAS NODRIZAS DICEN")
    print("Hay un total de " + str(contadorHormigas[2]) + " Nodrizas")
    print("==================================")
    print("\n")

    hormigaObrera()
    hormigaSepulturera()

    return()


#Función de la princesa
def hormigaPrincesa():

    print("**********************************")
    print("LAS PRINCESAS DICEN")
    print("Hay un total de " + str(contadorHormigas[3]) + " Princesas")
    print("**********************************")
    print("\n")

    return()


#Función del príncipe
def hormigaPrincipe():
    
    #En caso de estar en los meses de fecundación, el príncipe fecunda a más de una prinseca
    if( 9 <= mesDelAno <= 12 ):                         
        fecunda = random.randint(1,contadorHormigas[3])
        contadorHormigas[3] = contadorHormigas[3] - fecunda

        contadorHormigas[4] = contadorHormigas[4] - 1
        prnicipeExpulsado = contadorHormigas[4] - 1

        #Los datos de las princesas y príncipes fecundados se envían a la lsita expulsados.
        expulsados.append(fecunda)
        expulsados.append(contadorHormigas[4] - prnicipeExpulsado)


    print("++++++++++++++++++++++++++++++++++")
    print("LOS PRINCIPES DICEN")
    print("Hay un total de " + str(contadorHormigas[4]) + " Prícipes")
    print("++++++++++++++++++++++++++++++++++")
    print("\n")

    return()


#Función de la obrera
def hormigaObrera():
    print("//////////////////////////////////")
    print("LÍDER OBRERA DICE")
    print("hay un total de " + str(contadorHormigas[0]) + " Obreras")
    print("//////////////////////////////////")
    print("\n")
    return


#Funcion de la hormiga sepulturera
def hormigaSepulturera():
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("LAS SEPULTURERAS DICEN:")
    print("Hay un total de " + str(contadorHormigas[5]) + " Sepultureras")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("\n")
    return()

#Función del soldado
def hormigaSoldado( orden ):

    print("----------------------------------")
    print("GENERAL SOLDADO DICE:")
    print("Hay un total de " + str(contadorHormigas[1]) + " Soldados")
    print("\n")
    if(orden == 'Atacar'):
        print("La reina ordenó " + orden)
        print("----------------------------------")
        print("\n")
    else:
        print("La reina ordenó "+ orden)
        print("----------------------------------")
        print("\n")
    return();


#Esta es la sección principal donde se llama a el código en su totalidad.
print("\n")
print("Estamos en el mes " + str(mesDelAno) )
print("\n")

#Llamar a la hormiga reina genera el despliegue de información de las demás hormigas
hormigaReina()      

#En caso de encontrarnos en los meses de reproducción, se muestran los príncipes y princesas expulsados
if(9 <= mesDelAno <= 12):       
    print("Hay " + str(expulsados[0]) + " Princesas creando su hormiguero" )
    print("Hay " + str(expulsados[1]) + " Príncipes expulsados" )
print("\n")
