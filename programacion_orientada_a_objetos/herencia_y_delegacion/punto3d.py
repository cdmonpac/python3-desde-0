#!/usr/bin/python3
# Realizado por Carlos Montoya =)

""" 
Ejercicio de herencia

La herencia es un mecanismo de la programación orientada a objetos 
que sirve para crear clases nuevas a partir de clases preexistentes. 
Se toman (heredan) atributos y métodos de las clases bases 
y se los modifica para modelar una nueva situación.

La clase desde la que se hereda se llama clase base 
y la que se construye a partir de ella es una clase derivada.

Si nuestra clase base es la clase punto estudiadas en unidades anteriores,
puedo crear una nueva clase de la siguiente manera:
"""
from punto import punto
class punto3d(punto):
    def __init__(self,x=0,y=0,z=0):
        super().__init__(x,y)
        self.z=z

    @property
    def z(self):
        print("Doy z")
        return self.__z

    @z.setter
    def z(self,z):
        print("Cambio z")
        self.__z=z

    def mostrar(self):
       return super().mostrar()+":"+str(self.__z)

    def distancia(self,otro):
        dx = self.__x - otro.__x
        dy = self.__y - otro.__y
        dz = self.__z - otro.__z
        return (dx*dx + dy*dy + dz*dz)**0.5