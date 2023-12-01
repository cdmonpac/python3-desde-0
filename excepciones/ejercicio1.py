#!/usr/bin/python3
# Realizado por Carlos Montoya =)
      
while True:
    try:
        x = int(input("\nIntroduce un número: "))
        break
    except ValueError:
     	print ("No es un número válido, vuelve a intentarlo")