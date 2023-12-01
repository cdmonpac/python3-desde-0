#!/usr/bin/python3
# Realizado por Carlos Montoya =)

# Solo ponemos este ejercicio para que sirva de herencia a "punto3d"
import math
class punto():
    """ Representación de un punto en el plano, los atributos son x e y
    que representan los valores de las coordenadas cartesianas."""

    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    
    @property
    def x(self):
        print("Doy x")
        return self.__x
    
    @property
    def y(self):
        print("Doy y")
        return self.__y
       
    @x.setter
    def x(self,x):
        print("Cambio x")
        self.__x=x
    @y.setter
    def y(self,y):
        print("Cambio y")
        self.__y=y

    def mostrar(self):
        return str(self.__x)+":"+str(self.__y)
    
    def distancia(self, otro):
        """ Devuelve la distancia entre ambos puntos. """
        dx = self.__x - otro.__x
        dy = self.__y - otro.__y
        return math.sqrt((dx*dx + dy*dy))