#!/usr/bin/python3
# Realizado por Carlos Montoya =)

# Realizar un programa que compruebe si una cadena contiene una subcadena.
# Las dos cadenas se introducen por teclado.

cad = input("Introduce una cadena: ")
subcad = input("Introduce una subcadena: ")

# Una forma de hacerlo
# if cad.find(subcad) > -1:
# 	print("La cadena contiene la subcadena.")
# else:
# 	print("La cadena no contiene la subcadena.")

# Otra forma de comprobarlo

if subcad in cad:
	print("La cadena contiene la subcadena.")
else:
	print("La cadena no contiene la subcadena.")

