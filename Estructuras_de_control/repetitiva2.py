#!/usr/bin/python3
# Realizado por Carlos Montoya =)

secreto = "carlos123"
clave = input("Dime la clave: ")
while clave != secreto:
    print ("La contraseña es incorrecta")
    otra = input("¿Quiéres introducir otra clave (s/n)?: ")
    if otra == "n":
        break;
    clave = input("Dime la clave: ")
if clave == secreto:
    print("Bienvenido!!!")
print("Programa terminado")