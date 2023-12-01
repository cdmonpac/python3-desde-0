#!/usr/bin/python3
# Realizado por Carlos Montoya =)

# Escribe un programa que pida un nombre de usuario y una contraseña 
# y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema", 
# sino se da un error.

usuario = input("Introduce el usuario: ")
password = input("Introduce el password: ")
if usuario == "carlos" and password == "carlos123":
	print("Has entrado al sistema")
elif usuario != "carlos" and password != "carlos123":
	print("Uuario y password incorrectos")
elif usuario != "carlos":
	print("Usuario incorrecto")
else:
    print("Password incorrecta")
