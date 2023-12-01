#!/usr/bin/python3
# Realizado por Carlos Montoya =)

# Pide una cadena y un carácter por teclado (valida que sea un carácter) 
# y muestra cuantas veces aparece el carácter en la cadena.

cad = input("Introduce una cadena: ")
while True:
    car = input("Introduce un carácter: ")
    if len(car) > 1:
        print("Me tienes que dar un sólo carácter")
    if len(car) == 1: break
    
if cad.count(car) == 1:
    print("En la cadena",cad,"aparece",cad.count(car),"vez el carácter",car)
else:
    print("En la cadena",cad,"aparecen",cad.count(car),"veces el carácter",car)    