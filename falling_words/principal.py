#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *
pygame.init()

from configuracion import *
from extras import *
from funcionesSeparador import *
from funcionesVACIAS import *
import random

#Funcion principal
def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()

        #Preparar la ventana
        pygame.display.set_caption("Juego de Silabas - Grupo 19")
        screen = pygame.display.set_mode((ANCHO, ALTO))

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        vida = "<3 <3 <3 <3 <3 "
        puntos = 0
        candidata = ""
        silabasEnPantalla = []
        posiciones = []
        listaDeSilabas=[]
        lemario=[]

        archivo= open("silabas.txt","r")
        lectura(archivo, listaDeSilabas)

        archivo2= open("lemario.txt","r",encoding="latin-1")
        lectura(archivo2, lemario)


        dibujar(screen, candidata, silabasEnPantalla, posiciones, puntos,segundos, vida)

        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
            	fps = 3

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    candidata += letra
                    if e.key == K_BACKSPACE:
                        candidata = candidata[0:len(candidata)-1]
                    if e.key == K_RETURN:
                        puntos += procesar(candidata, silabasEnPantalla, posiciones, lemario)
                        ##valor de la cadena de vida actualizada por la funcion procesarVida
                        vida = procesarVida(candidata, silabasEnPantalla, posiciones, lemario,vida, puntos)
                        candidata = ""


            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo todo
            dibujar(screen, candidata, silabasEnPantalla, posiciones, puntos, segundos, vida)

            pygame.display.flip()

            actualizar(silabasEnPantalla, posiciones, listaDeSilabas)

        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()

##def menu():
##    d = False
##    while d == False:
##        print("------JUEGA DE LAS SILIBAS------\n")
##        print("------------OPCIONES------------","\n1.- JUGAR","\n2.- RECORDS","\n3.- SALIR")
##        pygame.mixer.music.load("mario-bross-version-metal-videojuegos.mp3")
##        pygame.mixer.music.play()
##        opcion = int(input(""))
##        if opcion == 1:
##            pygame.mixer.music.stop()
##            main()
##            d = True
##        if opcion == 2:
##            records()
##        if opcion == 3:
##            pygame.quit()
##            d = True
