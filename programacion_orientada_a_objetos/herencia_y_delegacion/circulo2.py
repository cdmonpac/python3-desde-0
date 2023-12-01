#!/usr/bin/python3
# Realizado por Carlos Montoya =)

'''
Delegación

Llamamos delegación a la situación en la que una clase contiene (como atributos)
una o más instancias de otra clase, a las que delegará parte de sus funcionalidades.

A partir de la clase punto, podemos crear la clase circulo de esta forma:
'''
class circulo():    

    def __init__(self,centro,radio):
        self.centro=centro
        self.radio=radio    

    def mostrar(self):
        return "Centro:{0}-Radio:{1}".format(self.centro.mostrar(),self.radio)