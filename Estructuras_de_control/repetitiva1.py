#!/usr/bin/python3
# Realizado por Carlos Montoya =)

secreto = "carlos123"
clave = input("Dime la clave: ")
while clave != secreto:
    print ("La contraseña es incorrecta")
    clave = input("Dime la clave: ")
print("Bienvenido!!!")
print("Programa terminado")