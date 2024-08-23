from principal import *
from configuracion import *
from funcionesSeparador import *

import random
import math
import pygame

def lectura(archivo, lista):
    for word in archivo.readlines():
        lista.append(word[:-1])
    return lista

def superpuesta(posiciones, posNewX):
    coord = posiciones[-1]
    a = False
    while a ==  False:
        if (coord[0]-150)<=posNewX:
            if posNewX<=(coord[0]+150):
                posNewX = random.randrange(30,ANCHO-30)
            else:
                a = True
        else:
            a = True
    return posNewX

def actualizar(silabasEnPantalla,posiciones,listaDeSilabas):
    silaba = nuevaSilaba(listaDeSilabas)
    silabasEnPantalla.append(silaba)

    posNewY = 0
    posNewX = random.randrange(30,ANCHO-30)
    if len(posiciones)>=1:
        posNewX = superpuesta(posiciones,posNewX)
    posNew = [posNewX,posNewY]
    posiciones.append(posNew)

    for pos in posiciones:
        pos[1] = pos[1] + 7
        if pos[1] >= ALTO-75:
            f = posiciones.index(pos)
            silabasEnPantalla.pop(f)
            posiciones.pop(f)

def nuevaSilaba(silabas):
    lista =[]
##    silabas = open("silabas.txt","r" )
##    lista = lectura(silabas,lista)
    return random.choice(silabas)

def quitar(candidata, silabasEnPantalla, posiciones):
    candidataList = dameSilabas(candidata)
    for silaba in candidataList:
        i = 0
        while (0 <= len(silabasEnPantalla)):
            if silaba == silabasEnPantalla[i]:
                silabasEnPantalla.pop(i)
                posiciones.pop(i)
                break
            i = i + 1

def dameSilabas(candidata):
    lista = []
    sil=""
    sil2=""
    c = 0
    a = separador(candidata)
    for i in range(0,len(a)):
        if a[i] != "-":
            sil = sil + a[i]
            c = c +1
        else:
            lista.append(sil)
            sil = ""
            c=0
    for i in range(len(candidata)-c,len(candidata)):
        sil2 = sil2 + candidata[i]
    lista.append(sil2)
    return lista


def esValida(candidata, silabasEnPantalla, lemario):
    lemario = open("lemario.txt","r",encoding="latin-1")
    listaux = []
    c = 0
    lista = lectura(lemario,listaux)
    silList = dameSilabas(candidata)
    if candidata in lista:
        for sil in silList:
            if sil in silabasEnPantalla:
                c = c +1
            else:
##      vida = vida[:-3]
                return False
        if c == len(silList):
            return True
    else:
##      vida = vida[:-3]
        return False

def Puntos(candidata):
    puntos = 0
    condif = ["j", "k", "q", "w", "x", "y", "z"]
    voc = ["a","e","i","o","u"]
    for word in candidata:
        if word in voc:
            puntos = puntos +1
        elif word in condif:
            puntos = puntos +5
        else:
            puntos = puntos +2
    return puntos

def procesarVida(candidata, silabasEnPantalla, posiciones, lemario,vida, puntos):
    vidaMenos = pygame.mixer.Sound("mario-bros-tuberia.mp3")
    gameOver = pygame.mixer.Sound("mario-bros-game-over.mp3")
    tof = esValida(candidata, silabasEnPantalla,lemario)
    if tof == False:
        vida = vida[:-3]
        vidaMenos.play()
    if len(vida) == 0:
        gameOver.play()
    return vida

##def gameOver (puntos):
##    print("Tu puntaje es",puntos,"\n1.- Guardar Puntaje","\n2.- Volve al Menu")
##    opcion = int(input(""))
##    if opcion == 1:
##        guardaRecord(puntos)
##    elif opcion == 2:
##        menu()

def procesar(candidata, silabasEnPantalla, posiciones, lemario):
    tof = esValida(candidata, silabasEnPantalla,lemario)
    if tof == True:
        quitar(candidata,silabasEnPantalla,posiciones)
        puntaje = Puntos(candidata)
    else:
        puntaje = 0
    return puntaje

##def guardaRecord():
##        archivo3 = open('record.txt','a')
##        nombre= input("Nombre del Jugador: ")
##        archivo3.write(nombre, '\n' , Puntos)
##        archivo3.close()

##def records():
##        archivo3 = open ('record.txt','r')
##        record = archivo3.read()
##        print(record)
##        archivo3.close()



