#!/usr/bin/python3
# Realizado por Carlos Montoya =)

secreto = "carlos123"
while True:
    clave = input("Dime la clave: ")
    if clave != secreto:
        print ("La contraseña es incorrecta")
    if clave == secreto:
        break
print("Bienvenido!!!")
print("Programa terminado")